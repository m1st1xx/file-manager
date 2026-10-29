"""Однократный перенос данных из SQLite (users.db, new_users.db) в PostgreSQL.

Запускается контейнером migrate перед стартом сервисов. Безопасен при
повторном запуске: после успешного переноса ставится отметка в таблице
public.sqlite_import, и следующие запуски ничего не делают.
Весь перенос идёт в одной транзакции — при ошибке в Postgres ничего не попадёт.

Что переносится:
  new_users.db: users    -> auth.users (id, username, password_hash)
                            files.storages (user_id, folder_path)
                subjects -> files.subjects
  users.db:     users    -> auth.legacy_users (вход старым способом)
                subjects -> auth.legacy_subjects
Таблицы groups/group_members не переносятся (функционал групп удалён).

Использование:
  python -m migration.migrate_sqlite_to_postgres [--old-db users.db] [--new-db new_users.db]
"""
import argparse
import os
import sqlite3
import sys
from pathlib import Path

import psycopg

ROOT_DIR = Path(__file__).resolve().parents[1]
SCHEMAS = [
    ROOT_DIR / "services" / "auth" / "schema.sql",
    ROOT_DIR / "services" / "files" / "schema.sql",
]


def log(message):
    print(f"[migrate] {message}", flush=True)


def open_sqlite(path):
    if not os.path.exists(path):
        log(f"{path} не найден — пропускаю")
        return None
    if not os.path.isfile(path):
        # docker создаёт каталог на месте несуществующего файла в volume
        raise SystemExit(f"[migrate] {path} — не файл. Проверьте volume в docker-compose.yml")
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def table_exists(conn, name):
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?", (name,)
    ).fetchone() is not None


def dedupe_usernames(users):
    """В new_users.db у username не было UNIQUE, поэтому возможны дубликаты.
    Вход всегда находил запись с наименьшим id, так что она сохраняет имя,
    а остальные (в которые и так нельзя было войти) переименовываются."""
    taken = {u["username"] for u in users}
    seen = set()
    renamed = []
    result = []

    for user in sorted(users, key=lambda u: u["id"]):
        username = user["username"]
        if username in seen:
            new_name = f"{username}_{user['id']}"
            counter = 1
            while new_name in taken:
                new_name = f"{username}_{user['id']}_{counter}"
                counter += 1
            taken.add(new_name)
            renamed.append((user["id"], username, new_name))
            username = new_name
        seen.add(username)
        result.append({**user, "username": username})

    return result, renamed


def set_identity(pg, table):
    pg.execute(
        f"""SELECT setval(pg_get_serial_sequence('{table}', 'id'),
                          COALESCE((SELECT MAX(id) FROM {table}), 0) + 1, false)"""
    )


def migrate(pg, old_db, new_db):
    stats = {}

    new_users = []
    if new_db and table_exists(new_db, "users"):
        new_users = [dict(r) for r in new_db.execute(
            "SELECT id, username, password_hash, folder_path FROM users ORDER BY id"
        )]
    new_users, renamed = dedupe_usernames(new_users)

    for user in new_users:
        pg.execute(
            "INSERT INTO auth.users (id, username, password_hash) VALUES (%s, %s, %s)",
            (user["id"], user["username"], user["password_hash"]),
        )
        pg.execute(
            "INSERT INTO files.storages (user_id, folder_path) VALUES (%s, %s)",
            (user["id"], user["folder_path"]),
        )
    stats["auth.users / files.storages"] = len(new_users)

    user_ids = {u["id"] for u in new_users}
    subjects = 0
    if new_db and table_exists(new_db, "subjects"):
        for row in new_db.execute("SELECT id, user_id, name FROM subjects ORDER BY id"):
            if row["user_id"] not in user_ids:
                continue
            pg.execute(
                """INSERT INTO files.subjects (id, user_id, name) VALUES (%s, %s, %s)
                   ON CONFLICT (user_id, name) DO NOTHING""",
                (row["id"], row["user_id"], row["name"]),
            )
            subjects += 1
    stats["files.subjects"] = subjects

    # Старый аккаунт считается перенесённым, если уже есть новый аккаунт
    # с той же папкой (так работал set_username в монолите)
    folder_owner = {}
    for user in new_users:
        folder_owner.setdefault(user["folder_path"], user["id"])

    legacy_ids = set()
    if old_db and table_exists(old_db, "users"):
        for row in old_db.execute(
            """SELECT id, first_name, last_name, group_number, password_hash, folder_path
               FROM users ORDER BY id"""
        ):
            pg.execute(
                """INSERT INTO auth.legacy_users
                   (id, first_name, last_name, group_number, password_hash, folder_path, migrated_user_id)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (
                    row["id"], row["first_name"], row["last_name"], row["group_number"],
                    row["password_hash"], row["folder_path"], folder_owner.get(row["folder_path"]),
                ),
            )
            legacy_ids.add(row["id"])
    stats["auth.legacy_users"] = len(legacy_ids)

    legacy_subjects = 0
    if old_db and table_exists(old_db, "subjects"):
        for row in old_db.execute("SELECT id, user_id, name FROM subjects ORDER BY id"):
            if row["user_id"] not in legacy_ids:
                continue
            pg.execute(
                """INSERT INTO auth.legacy_subjects (id, legacy_user_id, name) VALUES (%s, %s, %s)
                   ON CONFLICT (legacy_user_id, name) DO NOTHING""",
                (row["id"], row["user_id"], row["name"]),
            )
            legacy_subjects += 1
    stats["auth.legacy_subjects"] = legacy_subjects

    # id переносились явно — сдвигаем счётчики identity за максимальный id
    for table in ("auth.users", "auth.legacy_users", "auth.legacy_subjects", "files.subjects"):
        set_identity(pg, table)

    # Аккаунты, созданные через set_username, в монолите получали предметы
    # только при следующем перезапуске. Если у такого аккаунта предметов нет,
    # отдаём ему предметы старого аккаунта.
    inherited = pg.execute(
        """INSERT INTO files.subjects (user_id, name)
           SELECT lu.migrated_user_id, ls.name
           FROM auth.legacy_subjects ls
           JOIN auth.legacy_users lu ON lu.id = ls.legacy_user_id
           WHERE lu.migrated_user_id IS NOT NULL
             AND NOT EXISTS (SELECT 1 FROM files.subjects s WHERE s.user_id = lu.migrated_user_id)
           ORDER BY ls.id
           ON CONFLICT (user_id, name) DO NOTHING"""
    ).rowcount
    stats["files.subjects (из старых аккаунтов)"] = inherited

    return stats, renamed


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--old-db", default=os.getenv("OLD_SQLITE_PATH", "users.db"))
    parser.add_argument("--new-db", default=os.getenv("NEW_SQLITE_PATH", "new_users.db"))
    parser.add_argument("--database-url", default=os.getenv("DATABASE_URL"))
    args = parser.parse_args()

    if not args.database_url:
        raise SystemExit("[migrate] не задан DATABASE_URL")

    with psycopg.connect(args.database_url) as pg:
        pg.execute("SELECT pg_advisory_xact_lock(724501)")
        for schema in SCHEMAS:
            pg.execute(schema.read_text(encoding="utf-8"))
        pg.execute(
            """CREATE TABLE IF NOT EXISTS public.sqlite_import (
                   imported_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                   report TEXT NOT NULL
               )"""
        )

        if pg.execute("SELECT 1 FROM public.sqlite_import").fetchone():
            log("данные из SQLite уже перенесены ранее — пропускаю")
            return

        if pg.execute(
            "SELECT 1 FROM auth.users UNION ALL SELECT 1 FROM auth.legacy_users LIMIT 1"
        ).fetchone():
            raise SystemExit(
                "[migrate] в PostgreSQL уже есть пользователи, но отметки о переносе нет. "
                "Перенос остановлен, чтобы не смешать данные."
            )

        old_db = open_sqlite(args.old_db)
        new_db = open_sqlite(args.new_db)

        stats, renamed = migrate(pg, old_db, new_db)

        report_lines = [f"{table}: {count}" for table, count in stats.items()]
        for user_id, old_name, new_name in renamed:
            report_lines.append(f"дубликат имени: id={user_id} «{old_name}» -> «{new_name}»")
        report = "\n".join(report_lines)

        pg.execute("INSERT INTO public.sqlite_import (report) VALUES (%s)", (report,))

    for line in report_lines:
        log(line)
    log("перенос завершён")


if __name__ == "__main__":
    sys.exit(main())
