import sqlite3
import os
from pathlib import Path


UPLOAD_BASE = "uploads"
DEFAULT_SUBJECTS = ["ПОКС", "ОППиФКС", "ЭОСИ", "АСОС", "ОАКС", "ИКГ", "МПС"]


def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# создание новой бд только логин пароль путь

def get_new_db():
    conn = sqlite3.connect("new_users.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            group_number TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            folder_path TEXT NOT NULL
        )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            UNIQUE(user_id, name),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )"""
    )

    conn.commit()

    users = c.execute("SELECT id, folder_path FROM users").fetchall()

    for user in users:
        count = c.execute(
            "SELECT COUNT(*) FROM subjects WHERE user_id = ?",
            (user["id"],)
        ).fetchone()[0]

        if count == 0:
            for subject in DEFAULT_SUBJECTS:
                c.execute(
                    "INSERT OR IGNORE INTO subjects (user_id, name) VALUES (?, ?)",
                    (user["id"], subject)
                )
                Path(os.path.join(user["folder_path"], subject)).mkdir(
                    parents=True,
                    exist_ok=True
                )

    conn.commit()
    conn.close()

# создание таблиц для новой бд

def init_new_db():
    conn = get_new_db()
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            folder_path TEXT NOT NULL
        )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            UNIQUE(user_id, name),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )"""
    )

    conn.commit()

    users = c.execute("SELECT id, folder_path FROM users").fetchall()

    for user in users:
        count = c.execute(
            "SELECT COUNT(*) FROM subjects WHERE user_id = ?",
            (user["id"],)
        ).fetchone()[0]

        if count == 0:
            for subject in DEFAULT_SUBJECTS:
                c.execute(
                    "INSERT OR IGNORE INTO subjects (user_id, name) VALUES (?, ?)",
                    (user["id"], subject)
                )
                Path(os.path.join(user["folder_path"], subject)).mkdir(
                    parents=True,
                    exist_ok=True
                )

    conn.commit()
    conn.close()