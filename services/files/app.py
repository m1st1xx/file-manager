"""files-service: предметы пользователя, загрузка, скачивание и удаление файлов.

Владеет схемой files в PostgreSQL и папкой uploads на диске.
Внутреннее API (/internal/*) используют auth- и web-service.
"""
import os
import secrets
import string
from pathlib import Path

import psycopg
from flask import abort, flash, redirect, render_template, request, send_from_directory, session, url_for

from services.common.config import UPLOAD_BASE
from services.common.db import connection, init_schema
from services.common.filenames import safe_filename, unique_filename
from services.common.web import create_app, internal_only, register_routes

app = create_app(__name__)

init_schema((Path(__file__).parent / "schema.sql").read_text(encoding="utf-8"))


# Вспомогательные функции

def clean_subject_name(name):
    name = " ".join(name.strip().split())

    if not name or len(name) > 100:
        return None

    if "/" in name or "\\" in name or "\x00" in name:
        return None

    # «.» и «..» указывали бы на саму папку пользователя или на uploads/
    if name in (".", ".."):
        return None

    return name


def is_inside(base, path):
    base = os.path.abspath(base)
    return os.path.abspath(path).startswith(base + os.sep)


def generate_folder_path():
    while True:
        name = "".join(secrets.choice(string.ascii_letters) for _ in range(10))
        folder_path = os.path.join(UPLOAD_BASE, name)
        if not os.path.exists(folder_path):
            return folder_path


def get_subjects(user_id):
    with connection() as conn:
        rows = conn.execute(
            "SELECT name FROM files.subjects WHERE user_id = %s ORDER BY id",
            (user_id,),
        ).fetchall()
    return [row["name"] for row in rows]


def get_user_folder():
    with connection() as conn:
        row = conn.execute(
            "SELECT folder_path FROM files.storages WHERE user_id = %s",
            (session["user_id"],),
        ).fetchone()
    return row["folder_path"] if row else None


def get_subject_path(subject):
    """Абсолютный путь к папке предмета текущего пользователя или None."""
    user_folder = get_user_folder()
    if not user_folder or subject not in get_subjects(session["user_id"]):
        return None

    subject_path = os.path.abspath(os.path.join(user_folder, subject))
    if not is_inside(user_folder, subject_path):
        return None
    return subject_path


# Внутреннее API для других сервисов

@app.post("/internal/storages")
@internal_only
def internal_create_storage():
    data = request.get_json(force=True)
    user_id = int(data["user_id"])
    folder_path = data.get("folder_path")
    subjects = data.get("subjects") or []

    if folder_path and not is_inside(UPLOAD_BASE, folder_path):
        abort(400)

    with connection() as conn:
        existing = conn.execute(
            "SELECT folder_path FROM files.storages WHERE user_id = %s",
            (user_id,),
        ).fetchone()

        if existing:
            folder_path = existing["folder_path"]
        else:
            folder_path = folder_path or generate_folder_path()
            conn.execute(
                "INSERT INTO files.storages (user_id, folder_path) VALUES (%s, %s)",
                (user_id, folder_path),
            )

        Path(folder_path).mkdir(parents=True, exist_ok=True)

        # При переносе старого аккаунта предметами становятся его старые
        # предметы и уже существующие папки предметов с файлами
        existing_dirs = sorted(
            entry.name for entry in os.scandir(folder_path) if entry.is_dir()
        )
        for name in [*subjects, *existing_dirs]:
            subject = clean_subject_name(name)
            if not subject:
                continue
            conn.execute(
                """INSERT INTO files.subjects (user_id, name) VALUES (%s, %s)
                   ON CONFLICT (user_id, name) DO NOTHING""",
                (user_id, subject),
            )
            Path(folder_path, subject).mkdir(parents=True, exist_ok=True)

    return {"folder_path": folder_path}


@app.get("/internal/users/<int:user_id>/subjects")
@internal_only
def internal_user_subjects(user_id):
    return {"subjects": get_subjects(user_id)}


# Страницы

def edit_subjects():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    user_folder = get_user_folder()
    if not user_folder:
        session.clear()
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        subject = clean_subject_name(request.form.get("subject", ""))

        if not subject:
            flash("Введите корректное название предмета.", "error")
            return redirect(url_for("edit_subjects"))

        try:
            with connection() as conn:
                conn.execute(
                    "INSERT INTO files.subjects (user_id, name) VALUES (%s, %s)",
                    (session["user_id"], subject),
                )
            Path(user_folder, subject).mkdir(parents=True, exist_ok=True)
            flash(f"Предмет «{subject}» добавлен.", "success")

        except psycopg.errors.UniqueViolation:
            flash("Такой предмет уже добавлен.", "error")

        return redirect(url_for("edit_subjects"))

    return render_template("subjects.html", subjects=get_subjects(session["user_id"]))


def delete_subject():
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject = clean_subject_name(request.form.get("subject", ""))
    subject_path = get_subject_path(subject) if subject else None

    if not subject_path:
        flash("Предмет не найден.", "error")
        return redirect(url_for("edit_subjects"))

    if os.path.isdir(subject_path) and os.listdir(subject_path):
        flash(
            "Нельзя удалить предмет, пока в его папке есть файлы. "
            "Сначала удалите файлы.",
            "error",
        )
        return redirect(url_for("edit_subjects"))

    with connection() as conn:
        conn.execute(
            "DELETE FROM files.subjects WHERE user_id = %s AND name = %s",
            (session["user_id"], subject),
        )

    if os.path.isdir(subject_path):
        os.rmdir(subject_path)

    flash(f"Предмет «{subject}» удалён.", "success")
    return redirect(url_for("edit_subjects"))


def select_subject(mode):
    if "user_id" not in session:
        return redirect(url_for("index"))

    subjects = get_subjects(session["user_id"])
    if not subjects:
        return redirect(url_for("edit_subjects"))

    return render_template("select_subject.html", mode=mode, subjects=subjects)


def download_select():
    return select_subject("download")


def upload_select():
    return select_subject("upload")


def subject_files(mode, subject):
    if mode not in ["download", "upload"]:
        return "НЕВЕРНЫЙ РЕЖИМ", 400

    if "user_id" not in session:
        return redirect(url_for("index"))

    subject_path = get_subject_path(subject)
    if not subject_path:
        return "НЕПРАВИЛЬНЫЙ ПРЕДМЕТ", 400

    Path(subject_path).mkdir(parents=True, exist_ok=True)
    page_url = url_for("subject_files", mode=mode, subject=subject)

    if request.method == "POST" and mode == "upload":
        file = request.files.get("file")

        if not file or not file.filename:
            flash("ФАЙЛ НЕ ВЫБРАН", "error")
            return redirect(page_url)

        filename = safe_filename(file.filename)

        if not filename:
            flash("НЕКОРРЕКТНОЕ ИМЯ ФАЙЛА", "error")
            return redirect(page_url)

        filename = unique_filename(subject_path, filename)
        file.save(os.path.join(subject_path, filename))

        flash("ФАЙЛ УСПЕШНО ЗАГРУЖЕН", "success")
        return redirect(page_url)

    files = sorted(
        f for f in os.listdir(subject_path)
        if os.path.isfile(os.path.join(subject_path, f))
    )

    return render_template("subject_files.html", mode=mode, subject=subject, files=files)


def delete_file(subject, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject_path = get_subject_path(subject)
    if not subject_path:
        return "INCORRECT SUBJECT", 400

    file_path = os.path.join(subject_path, filename)
    if not is_inside(subject_path, file_path):
        return "INCORRECT FILE", 400

    if os.path.isfile(file_path):
        os.remove(file_path)
        flash(f"Файл '{filename}' удалён.", "success")
    else:
        flash("Файл не найден.", "error")

    return redirect(url_for("subject_files", mode="upload", subject=subject))


def download_file(subject, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject_path = get_subject_path(subject)
    if not subject_path:
        return "INCORRECT SUBJECT", 400

    file_path = os.path.join(subject_path, filename)
    if not is_inside(subject_path, file_path):
        return "INCORRECT FILE", 400

    if not os.path.isfile(file_path):
        return "ФАЙЛ НЕ НАЙДЕН", 404

    # Для не-ASCII имён Flask сам выставит Content-Disposition с filename*=UTF-8''...
    return send_from_directory(subject_path, filename, as_attachment=True)


register_routes(app, "files", {
    "edit_subjects": edit_subjects,
    "delete_subject": delete_subject,
    "download_select": download_select,
    "upload_select": upload_select,
    "subject_files": subject_files,
    "delete_file": delete_file,
    "download_file": download_file,
})
