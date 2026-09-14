from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import sqlite3
import os
import random
import string
from urllib.parse import unquote
from pathlib import Path
from dotenv import load_dotenv
from os import getenv
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from database import get_db, get_new_db, init_db, init_new_db

app = Flask(__name__)

load_dotenv()
TOKEN = getenv("TOKEN")
app.secret_key = TOKEN

UPLOAD_BASE = "uploads"
DEFAULT_SUBJECTS = ["ПОКС", "ОППиФКС", "ЭОСИ", "АСОС", "ОАКС", "ИКГ", "МПС"]

# Автоматическая инициализация баз данных при запуске
init_db()
init_new_db()


# Вспомогательные функции групп

def generate_group_code():
    """Генерация уникального 10-значного ID группы"""
    conn = get_new_db()
    chars = string.ascii_letters + string.digits
    while True:
        code = "".join(random.choices(chars, k=10))
        exists = conn.execute("SELECT 1 FROM groups WHERE group_code = ?", (code,)).fetchone()
        if not exists:
            conn.close()
            return code

def get_user_groups(user_id):
    """Получить список всех групп, в которых состоит пользователь"""
    conn = get_new_db()
    rows = conn.execute(
        """SELECT g.id, g.group_code, g.name, g.created_by, gm.is_admin
           FROM groups g
           JOIN group_members gm ON g.id = gm.group_id
           WHERE gm.user_id = ?
           ORDER BY g.id DESC""",
        (user_id,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def is_group_member(group_id, user_id):
    """Проверка, является ли пользователь участником группы"""
    conn = get_new_db()
    row = conn.execute(
        "SELECT 1 FROM group_members WHERE group_id = ? AND user_id = ?",
        (group_id, user_id)
    ).fetchone()
    conn.close()
    return row is not None

def is_group_admin(group_id, user_id):
    """Проверка, является ли пользователь администратором группы"""
    conn = get_new_db()
    row = conn.execute(
        "SELECT is_admin FROM group_members WHERE group_id = ? AND user_id = ?",
        (group_id, user_id)
    ).fetchone()
    conn.close()
    return row and row["is_admin"] == 1


def get_current_user():
    if "user_id" not in session:
        return None

    conn = get_new_db()
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

    conn = get_new_db()
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

    if "/" in name or "\\" in name or "\x00" in name:
        return None

    return name


def create_subject_folder(subject):
    user_folder = get_user_folder()

    if user_folder:
        Path(os.path.join(user_folder, subject)).mkdir(parents=True, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"].strip()
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]
    if password != password_confirm:
        flash("Пароли не совпадают.", "error")
        return redirect(url_for("index"))
    password_hash = generate_password_hash(password)

    folder_path = os.path.join(
        UPLOAD_BASE,
        "".join(random.sample(string.ascii_letters, 10))
    )

    try:
        conn = get_new_db()
        conn.execute(
            """INSERT INTO users
               (username, password_hash, folder_path)
               VALUES (?, ?, ?)""",
            (
                username,
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
            "Пользователь с таким именем уже существует.",
            "error"
        )

    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"].strip()
    password = request.form["password"]

    conn = get_new_db()

    user = conn.execute(
        """SELECT * FROM users
           WHERE username = ? """,
        (username, )
    ).fetchone()

    conn.close()

    if user and check_password_hash(user["password_hash"], password):
        session.clear()
        session["user_id"] = user["id"]
        session["user"] = f"{user['username']}"

        if not get_user_subjects():
            return redirect(url_for("edit_subjects"))

        return redirect(url_for("main"))

    flash("Неверные данные", "error")
    return redirect(url_for("index"))


@app.route("/old_login", methods=["POST"])
def old_login():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    group_number = request.form["group_number"].strip()
    password = request.form["old_password"]

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

        return redirect(url_for("set_username"))

    flash("Неверные данные", "error")
    return redirect(url_for("index"))


@app.route("/set_username", methods=["GET","POST"])
def set_username():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("set_username.html")

    username = request.form["username"].strip()
    conn = get_db()
    password_row = conn.execute(
        """SELECT password_hash FROM users WHERE first_name = ? AND last_name = ? """,
        (session['first_name'], session['last_name'])
    ).fetchone()

    folder_row = conn.execute(
        """SELECT folder_path FROM users WHERE first_name = ? AND last_name = ? """,
        (session['first_name'], session['last_name'])
    ).fetchone()
    conn.close()

    password_hash = password_row["password_hash"]
    folder_path = folder_row["folder_path"]

    conn = get_new_db()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO users
           (username, password_hash, folder_path)
           VALUES (?, ?, ?)""",
        (
            username,
            password_hash,
            folder_path
        )
    )
    conn.commit()
    new_user_id = cursor.lastrowid
    conn.close()

    session["user_id"] = new_user_id
    session["user"] = username
    flash("Имя пользователя успешно обновлено!", "success")
    return redirect(url_for("main"))


@app.route("/main")
def main():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    if not get_user_subjects():
        return redirect(url_for("edit_subjects"))

    user_groups = get_user_groups(session["user_id"])
    return render_template("main.html", user_groups=user_groups)


@app.route("/create_group", methods=["POST"])
def create_group():
    if "user_id" not in session:
        return redirect(url_for("index"))

    group_name = clean_subject_name(request.form.get("name", ""))
    if not group_name:
        flash("Введите корректное название группы.", "error")
        return redirect(url_for("main"))

    group_code = generate_group_code()
    group_folder = os.path.join(UPLOAD_BASE, "groups", group_code)

    Path(group_folder).mkdir(parents=True, exist_ok=True)

    conn = get_new_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO groups (group_code, name, created_by, folder_path) VALUES (?, ?, ?, ?)",
        (group_code, group_name, session["user_id"], group_folder)
    )
    group_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO group_members (group_id, user_id, is_admin) VALUES (?, ?, 1)",
        (group_id, session["user_id"])
    )
    conn.commit()
    conn.close()

    flash(f"Группа «{group_name}» создана! ID группы: {group_code}", "success")
    return redirect(url_for("group_page", group_id=group_id))


@app.route("/join_group", methods=["POST"])
def join_group():
    if "user_id" not in session:
        return redirect(url_for("index"))

    group_code = request.form.get("group_code", "").strip()

    if not group_code or len(group_code) != 10:
        flash("Введите правильный 10-значный ID группы.", "error")
        return redirect(url_for("main"))

    conn = get_new_db()
    group = conn.execute(
        "SELECT * FROM groups WHERE group_code = ?",
        (group_code,)
    ).fetchone()

    if not group:
        conn.close()
        flash("Группа с таким ID не найдена.", "error")
        return redirect(url_for("main"))

    already_member = conn.execute(
        "SELECT 1 FROM group_members WHERE group_id = ? AND user_id = ?",
        (group["id"], session["user_id"])
    ).fetchone()

    if already_member:
        conn.close()
        flash("Вы уже состоите в этой группе.", "error")
        return redirect(url_for("group_page", group_id=group["id"]))

    conn.execute(
        "INSERT INTO group_members (group_id, user_id, is_admin) VALUES (?, ?, 0)",
        (group["id"], session["user_id"])
    )
    conn.commit()
    conn.close()

    flash(f"Вы присоединились к группе «{group['name']}»!", "success")
    return redirect(url_for("group_page", group_id=group["id"]))


@app.route("/group/<int:group_id>")
def group_page(group_id):
    if "user_id" not in session:
        return redirect(url_for("index"))

    if not is_group_member(group_id, session["user_id"]):
        flash("У вас нет доступа к этой группе.", "error")
        return redirect(url_for("main"))

    conn = get_new_db()
    group = conn.execute("SELECT * FROM groups WHERE id = ?", (group_id,)).fetchone()

    if not group:
        conn.close()
        flash("Группа не найдена.", "error")
        return redirect(url_for("main"))

    is_admin = is_group_admin(group_id, session["user_id"])

    members = []
    if is_admin:
        members = conn.execute(
            """SELECT u.id, u.username, gm.is_admin
               FROM users u
               JOIN group_members gm ON u.id = gm.user_id
               WHERE gm.group_id = ?""",
            (group_id,)
        ).fetchall()

    conn.close()

    group_folder = group["folder_path"]
    Path(group_folder).mkdir(parents=True, exist_ok=True)
    files = [f for f in os.listdir(group_folder) if os.path.isfile(os.path.join(group_folder, f))]

    return render_template(
        "group.html",
        group=group,
        is_admin=is_admin,
        files=files,
        members=members
    )


@app.route("/group/<int:group_id>/upload", methods=["POST"])
def group_upload_file(group_id):
    if "user_id" not in session:
        return redirect(url_for("index"))

    if not is_group_admin(group_id, session["user_id"]):
        flash("Только администраторы группы могут загружать файлы.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    conn = get_new_db()
    group = conn.execute("SELECT * FROM groups WHERE id = ?", (group_id,)).fetchone()
    conn.close()

    if not group:
        flash("Группа не найдена.", "error")
        return redirect(url_for("main"))

    if "file" not in request.files:
        flash("Файл не выбран.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    file = request.files["file"]
    if not file.filename:
        flash("Файл не выбран.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    filename = secure_filename(file.filename)
    if not filename:
        flash("Некорректное имя файла.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    file.save(os.path.join(group["folder_path"], filename))

    flash("Файл успешно загружен в группу!", "success")
    return redirect(url_for("group_page", group_id=group_id))


@app.route("/group/<int:group_id>/download/<path:filename>")
def group_download_file(group_id, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    if not is_group_member(group_id, session["user_id"]):
        return "НЕТ ДОСТУПА", 403

    conn = get_new_db()
    group = conn.execute("SELECT * FROM groups WHERE id = ?", (group_id,)).fetchone()
    conn.close()

    if not group:
        return "ГРУППА НЕ НАЙДЕНА", 404

    filename = unquote(filename)
    group_folder = os.path.abspath(group["folder_path"])
    file_path = os.path.abspath(os.path.join(group_folder, filename))

    if not file_path.startswith(group_folder + os.sep):
        return "НЕКОРРЕКТНЫЙ ФАЙЛ", 400

    if not os.path.isfile(file_path):
        return "ФАЙЛ НЕ НАЙДЕН", 404

    return send_from_directory(group_folder, filename, as_attachment=True)


@app.route("/group/<int:group_id>/delete_file/<path:filename>", methods=["POST"])
def group_delete_file(group_id, filename):
    if "user_id" not in session:
        return redirect(url_for("index"))

    if not is_group_admin(group_id, session["user_id"]):
        flash("Только администраторы могут удалять файлы.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    conn = get_new_db()
    group = conn.execute("SELECT * FROM groups WHERE id = ?", (group_id,)).fetchone()
    conn.close()

    if not group:
        flash("Группа не найдена.", "error")
        return redirect(url_for("main"))

    filename = unquote(filename)
    group_folder = os.path.abspath(group["folder_path"])
    file_path = os.path.abspath(os.path.join(group_folder, filename))

    if not file_path.startswith(group_folder + os.sep):
        return "НЕКОРРЕКТНЫЙ ФАЙЛ", 400

    if os.path.isfile(file_path):
        os.remove(file_path)
        flash(f"Файл '{filename}' удалён из группы.", "success")
    else:
        flash("Файл не найден.", "error")

    return redirect(url_for("group_page", group_id=group_id))


@app.route("/group/<int:group_id>/assign_admin", methods=["POST"])
def assign_admin(group_id):
    if "user_id" not in session:
        return redirect(url_for("index"))

    if not is_group_admin(group_id, session["user_id"]):
        flash("У вас нет прав администратора.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    user_ids = request.form.getlist("user_ids")
    if not user_ids:
        flash("Не выбрано ни одного участника.", "error")
        return redirect(url_for("group_page", group_id=group_id))

    conn = get_new_db()
    for uid in user_ids:
        conn.execute(
            "UPDATE group_members SET is_admin = 1 WHERE group_id = ? AND user_id = ?",
            (group_id, uid)
        )
    conn.commit()
    conn.close()

    flash("Выбранные участники успешно назначены администраторами!", "success")
    return redirect(url_for("group_page", group_id=group_id))


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

        conn = get_new_db()

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

    if os.path.isdir(subject_path) and os.listdir(subject_path):
        flash(
            "Нельзя удалить предмет, пока в его папке есть файлы. "
            "Сначала удалите файлы.",
            "error"
        )
        return redirect(url_for("edit_subjects"))

    conn = get_new_db()

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


@app.route("/delete_file/<path:subject>/<path:filename>", methods=["POST"])
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
        username = request.form["username"]
        new_password = request.form["new_password"]

        conn = get_new_db()

        user = conn.execute(
            """SELECT id FROM users
               WHERE username = ? """,
            (username, )
        ).fetchone()

        if user:
            password_hash = generate_password_hash(new_password)

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