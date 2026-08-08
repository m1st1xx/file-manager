from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import sqlite3
import os
from urllib.parse import unquote
from pathlib import Path
from dotenv import load_dotenv
from os import getenv
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)

load_dotenv()
TOKEN=getenv("TOKEN")
app.secret_key = TOKEN

UPLOAD_BASE = "uploads"
DEFAULT_SUBJECTS = ["ПОКС", "ОППиФКС", "ЭОСИ", "АСОС", "ОАКС", "ИКГ", "МПС"]


def get_db():
    conn = sqlite3.connect("users.db")
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

    # обратная совместимость для старых пользователей, люблю вас)
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


def get_current_user():
    if "user_id" not in session:
        return None

    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (session["user_id"],)
    ).fetchone()
    conn.close()
    return user


def get_user_folder():
    user = get_current_user()
    return user["folder_path"] if user else None


def get_user_subjects():
    if "user_id" not in session:
        return []

    conn = get_db()
    rows = conn.execute(
        "SELECT name FROM subjects WHERE user_id = ? ORDER BY id",
        (session["user_id"],)
    ).fetchall()
    conn.close()

    return [row["name"] for row in rows]


def subject_exists_for_user(subject):
    return subject in get_user_subjects()


def clean_subject_name(name):
    name = " ".join(name.strip().split())

    if not name or len(name) > 100:
        return None

    # Запрет символов, которые могут превратить название в путь.
    if "/" in name or "\\" in name or "\x00" in name:
        return None

    return name


def create_subject_folder(subject):
    user_folder = get_user_folder()

    if user_folder:
        Path(os.path.join(user_folder, subject)).mkdir(parents=True,exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    group_number = request.form["group_number"].strip()
    password_hash = generate_password_hash(request.form["password"])

    folder_path = os.path.join(
        UPLOAD_BASE,
        f"{first_name}_{last_name}"
    )

    try:
        conn = get_db()

        conn.execute(
            """INSERT INTO users
               (first_name, last_name, group_number, password_hash, folder_path)
               VALUES (?, ?, ?, ?, ?)""",
            (
                first_name,
                last_name,
                group_number,
                password_hash,
                folder_path
            )
        )

        Path(folder_path).mkdir(parents=True, exist_ok=True)

        conn.commit()
        conn.close()

        flash(
            "Аккаунт создан! Теперь войдите и добавьте свои предметы.",
            "success"
        )

    except sqlite3.IntegrityError:
        flash(
            "Пользователь с таким именем и фамилией уже существует.",
            "error"
        )

    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    group_number = request.form["group_number"].strip()
    password = request.form["password"]

    conn = get_db()

    user = conn.execute(
        """SELECT * FROM users
           WHERE first_name = ? AND last_name = ? AND group_number = ?""",
        (first_name, last_name, group_number)
    ).fetchone()

    conn.close()

    if user and check_password_hash(user["password_hash"], password):
        session.clear()
        session["user_id"] = user["id"]
        session["user"] = f"{user['first_name']} {user['last_name']}"
        session["first_name"] = user["first_name"]
        session["last_name"] = user["last_name"]

        if not get_user_subjects():
            return redirect(url_for("edit_subjects"))

        return redirect(url_for("main"))

    flash("Неверные данные", "error")
    return redirect(url_for("index"))


@app.route("/main")
def main():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if not get_user_subjects():
        return redirect(url_for("edit_subjects"))

    return render_template("main.html")


@app.route("/subjects", methods=["GET", "POST"])
def edit_subjects():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        subject = clean_subject_name(
            request.form.get("subject", "")
        )

        if not subject:
            flash("Введите корректное название предмета.", "error")
            return redirect(url_for("edit_subjects"))

        conn = get_db()

        try:
            conn.execute(
                "INSERT INTO subjects (user_id, name) VALUES (?, ?)",
                (session["user_id"], subject)
            )

            conn.commit()
            create_subject_folder(subject)

            flash(
                f"Предмет «{subject}» добавлен.",
                "success"
            )

        except sqlite3.IntegrityError:
            flash(
                "Такой предмет уже добавлен.",
                "error"
            )

        finally:
            conn.close()

        return redirect(url_for("edit_subjects"))

    return render_template(
        "subjects.html",
        subjects=get_user_subjects()
    )


@app.route("/subjects/delete", methods=["POST"])
def delete_subject():
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject = clean_subject_name(
        request.form.get("subject", "")
    )

    if not subject or not subject_exists_for_user(subject):
        flash("Предмет не найден.", "error")
        return redirect(url_for("edit_subjects"))

    user_folder = get_user_folder()
    subject_path = os.path.join(user_folder, subject)

    # Не удаляем предмет, если в его папке есть файлы.
    if os.path.isdir(subject_path) and os.listdir(subject_path):
        flash(
            "Нельзя удалить предмет, пока в его папке есть файлы. "
            "Сначала удалите файлы.",
            "error"
        )
        return redirect(url_for("edit_subjects"))

    conn = get_db()

    conn.execute(
        "DELETE FROM subjects WHERE user_id = ? AND name = ?",
        (session["user_id"], subject)
    )

    conn.commit()
    conn.close()

    if os.path.isdir(subject_path):
        os.rmdir(subject_path)

    flash(
        f"Предмет «{subject}» удалён.",
        "success"
    )

    return redirect(url_for("edit_subjects"))


@app.route("/download")
def download_select():
    if "user_id" not in session:
        return redirect(url_for("index"))

    subjects = get_user_subjects()

    if not subjects:
        return redirect(url_for("edit_subjects"))

    return render_template(
        "select_subject.html",
        mode="download",
        subjects=subjects
    )


@app.route("/upload")
def upload_select():
    if "user_id" not in session:
        return redirect(url_for("index"))

    subjects = get_user_subjects()

    if not subjects:
        return redirect(url_for("edit_subjects"))

    return render_template(
        "select_subject.html",
        mode="upload",
        subjects=subjects
    )


@app.route("/<mode>/<path:subject>", methods=["GET", "POST"])
def subject_files(subject, mode):
    if mode not in ["download", "upload"]:
        return "НЕВЕРНЫЙ РЕЖИМ", 400

    if "user_id" not in session:
        return redirect(url_for("index"))

    subject = unquote(subject)

    if not subject_exists_for_user(subject):
        return "НЕПРАВИЛЬНЫЙ ПРЕДМЕТ", 400

    user_folder = get_user_folder()
    subject_path = os.path.join(user_folder, subject)

    Path(subject_path).mkdir(
        parents=True,
        exist_ok=True
    )

    if request.method == "POST" and mode == "upload":
        if "file" not in request.files:
            flash("ФАЙЛ НЕ ВЫБРАН", "error")
            return redirect(request.url)

        file = request.files["file"]

        if not file.filename:
            flash("ФАЙЛ НЕ ВЫБРАН", "error")
            return redirect(request.url)

        filename = secure_filename(file.filename)

        if not filename:
            flash("НЕКОРРЕКТНОЕ ИМЯ ФАЙЛА", "error")
            return redirect(request.url)

        file.save(
            os.path.join(subject_path, filename)
        )

        flash(
            "ФАЙЛ УСПЕШНО ЗАГРУЖЕН",
            "success"
        )

        return redirect(request.url)

    files = [
        f
        for f in os.listdir(subject_path)
        if os.path.isfile(os.path.join(subject_path, f))
    ]

    return render_template(
        "subject_files.html",
        mode=mode,
        subject=subject,
        files=files
    )


@app.route("/delete_file/<path:subject>/<path:filename>",methods=["POST"])
def delete_file(subject, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject = unquote(subject)
    filename = unquote(filename)

    if not subject_exists_for_user(subject):
        return "INCORRECT SUBJECT", 400

    user_folder = get_user_folder()

    subject_path = os.path.abspath(
        os.path.join(user_folder, subject)
    )

    file_path = os.path.abspath(
        os.path.join(subject_path, filename)
    )

    if not file_path.startswith(subject_path + os.sep):
        return "INCORRECT FILE", 400

    if os.path.isfile(file_path):
        os.remove(file_path)
        flash(
            f"Файл '{filename}' удалён.",
            "success"
        )
    else:
        flash(
            "Файл не найден.",
            "error"
        )

    return redirect(
        url_for(
            "subject_files",
            mode="upload",
            subject=subject
        )
    )


@app.route("/download_file/<path:subject>/<path:filename>")
def download_file(subject, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    subject = unquote(subject)
    filename = unquote(filename)

    if not subject_exists_for_user(subject):
        return "INCORRECT SUBJECT", 400

    user_folder = get_user_folder()

    subject_path = os.path.abspath(
        os.path.join(user_folder, subject)
    )

    file_path = os.path.abspath(
        os.path.join(subject_path, filename)
    )

    if not file_path.startswith(subject_path + os.sep):
        return "INCORRECT FILE", 400

    if not os.path.isfile(file_path):
        return "ФАЙЛ НЕ НАЙДЕН", 404

    return send_from_directory(
        subject_path,
        filename,
        as_attachment=True
    )


@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        group_number = request.form["group_number"]
        new_password = request.form["new_password"]

        conn = get_db()

        user = conn.execute(
            """SELECT id FROM users
               WHERE first_name = ? AND last_name = ? AND group_number = ?""",
            (first_name, last_name, group_number)
        ).fetchone()

        if user:
            password_hash = generate_password_hash(
                new_password
            )

            conn.execute(
                "UPDATE users SET password_hash = ? WHERE id = ?",
                (password_hash, user["id"])
            )

            conn.commit()

            flash(
                "Пароль успешно изменён!",
                "success"
            )
        else:
            flash(
                "Пользователь не найден.",
                "error"
            )

        conn.close()

        return redirect(url_for("index"))

    return render_template("reset_password.html")


@app.context_processor
def inject_subjects():
    return {
        "SUBJECTS": get_user_subjects()
    }


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=False,host="0.0.0.0",port=5000)
