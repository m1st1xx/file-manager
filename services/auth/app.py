"""auth-service: регистрация, вход (в т.ч. старым способом), выбор имени
пользователя для старых аккаунтов, сброс пароля, выход.

Владеет схемой auth в PostgreSQL. Папки и предметы пользователей
создаются через внутреннее API files-service.
"""
from pathlib import Path

import psycopg
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from services.common import files_client
from services.common.db import connection, init_schema
from services.common.web import create_app, register_routes

app = create_app(__name__)

init_schema((Path(__file__).parent / "schema.sql").read_text(encoding="utf-8"))

MAX_USERNAME_LENGTH = 100


def clean_username(username):
    username = username.strip()
    if not username or len(username) > MAX_USERNAME_LENGTH:
        return None
    return username


def login_user(user_id, username):
    session.clear()
    session["user_id"] = user_id
    session["user"] = username


def index():
    return render_template("index.html")


def register():
    username = clean_username(request.form["username"])
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]

    if not username:
        flash("Введите корректное имя пользователя.", "error")
        return redirect(url_for("index"))

    if password != password_confirm:
        flash("Пароли не совпадают.", "error")
        return redirect(url_for("index"))

    try:
        with connection() as conn:
            user = conn.execute(
                """INSERT INTO auth.users (username, password_hash)
                   VALUES (%s, %s) RETURNING id""",
                (username, generate_password_hash(password)),
            ).fetchone()
            # Если files-service не создал папку — транзакция откатится
            files_client.create_storage(user["id"])

        flash("Аккаунт создан! Теперь войдите и добавьте свои предметы.", "success")

    except psycopg.errors.UniqueViolation:
        flash("Пользователь с таким именем уже существует.", "error")

    except files_client.FilesServiceError:
        app.logger.exception("files-service недоступен при регистрации")
        flash("Сервис временно недоступен, попробуйте позже.", "error")

    return redirect(url_for("index"))


def login():
    username = request.form["username"].strip()
    password = request.form["password"]

    with connection() as conn:
        user = conn.execute(
            "SELECT * FROM auth.users WHERE username = %s",
            (username,),
        ).fetchone()

    if user and check_password_hash(user["password_hash"], password):
        login_user(user["id"], user["username"])
        # Если предметов нет, web-service сам отправит на страницу предметов
        return redirect(url_for("main"))

    flash("Неверные данные", "error")
    return redirect(url_for("index"))


def old_login():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    group_number = request.form["group_number"].strip()
    password = request.form["old_password"]

    with connection() as conn:
        candidates = conn.execute(
            """SELECT * FROM auth.legacy_users
               WHERE first_name = %s AND last_name = %s AND group_number = %s
               ORDER BY id""",
            (first_name, last_name, group_number),
        ).fetchall()

        legacy = next(
            (u for u in candidates if check_password_hash(u["password_hash"], password)),
            None,
        )

        migrated = None
        if legacy and legacy["migrated_user_id"]:
            migrated = conn.execute(
                "SELECT id, username FROM auth.users WHERE id = %s",
                (legacy["migrated_user_id"],),
            ).fetchone()

    if not legacy:
        flash("Неверные данные", "error")
        return redirect(url_for("index"))

    # Имя пользователя уже выбрано раньше — входим в тот аккаунт,
    # а не создаём ещё один
    if migrated:
        login_user(migrated["id"], migrated["username"])
        flash(
            f"Ваш аккаунт уже переведён на вход по имени пользователя «{migrated['username']}».",
            "success",
        )
        return redirect(url_for("main"))

    session.clear()
    session["legacy_user_id"] = legacy["id"]
    session["user"] = f"{legacy['first_name']} {legacy['last_name']}"
    return redirect(url_for("set_username"))


def set_username():
    legacy_user_id = session.get("legacy_user_id")

    if not legacy_user_id:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("set_username.html")

    username = clean_username(request.form["username"])
    if not username:
        flash("Введите корректное имя пользователя.", "error")
        return redirect(url_for("set_username"))

    try:
        with connection() as conn:
            legacy = conn.execute(
                "SELECT * FROM auth.legacy_users WHERE id = %s FOR UPDATE",
                (legacy_user_id,),
            ).fetchone()

            if not legacy:
                session.clear()
                flash("Сначала войдите!", "error")
                return redirect(url_for("index"))

            if legacy["migrated_user_id"]:
                user = conn.execute(
                    "SELECT id, username FROM auth.users WHERE id = %s",
                    (legacy["migrated_user_id"],),
                ).fetchone()
                if user:
                    login_user(user["id"], user["username"])
                    return redirect(url_for("main"))

            subjects = [
                row["name"]
                for row in conn.execute(
                    "SELECT name FROM auth.legacy_subjects WHERE legacy_user_id = %s ORDER BY id",
                    (legacy["id"],),
                ).fetchall()
            ]

            user = conn.execute(
                """INSERT INTO auth.users (username, password_hash)
                   VALUES (%s, %s) RETURNING id""",
                (username, legacy["password_hash"]),
            ).fetchone()

            # Новый аккаунт получает старую папку с файлами и старые предметы
            files_client.create_storage(
                user["id"],
                folder_path=legacy["folder_path"],
                subjects=subjects,
            )

            conn.execute(
                "UPDATE auth.legacy_users SET migrated_user_id = %s WHERE id = %s",
                (user["id"], legacy["id"]),
            )

    except psycopg.errors.UniqueViolation:
        flash("Пользователь с таким именем уже существует.", "error")
        return redirect(url_for("set_username"))

    except files_client.FilesServiceError:
        app.logger.exception("files-service недоступен при переносе аккаунта")
        flash("Сервис временно недоступен, попробуйте позже.", "error")
        return redirect(url_for("set_username"))

    login_user(user["id"], username)
    flash("Имя пользователя успешно обновлено!", "success")
    return redirect(url_for("main"))


def reset_password():
    if request.method == "POST":
        username = request.form["username"]
        new_password = request.form["new_password"]

        with connection() as conn:
            user = conn.execute(
                "SELECT id FROM auth.users WHERE username = %s",
                (username,),
            ).fetchone()

            if user:
                conn.execute(
                    "UPDATE auth.users SET password_hash = %s WHERE id = %s",
                    (generate_password_hash(new_password), user["id"]),
                )

        if user:
            flash("Пароль успешно изменён!", "success")
        else:
            flash("Пользователь не найден.", "error")

        return redirect(url_for("index"))

    return render_template("reset_password.html")


def logout():
    session.clear()
    return redirect(url_for("index"))


register_routes(app, "auth", {
    "index": index,
    "register": register,
    "login": login,
    "old_login": old_login,
    "set_username": set_username,
    "reset_password": reset_password,
    "logout": logout,
})
