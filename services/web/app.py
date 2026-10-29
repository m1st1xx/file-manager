"""web-service: главная страница личного кабинета.

Своих данных не хранит; список предметов берёт у files-service.
"""
from flask import flash, redirect, render_template, session, url_for

from services.common import files_client
from services.common.web import create_app, register_routes

app = create_app(__name__)


def main():
    if "user_id" not in session:
        flash("Сначала войдите!", "error")
        return redirect(url_for("index"))

    try:
        subjects = files_client.get_subjects(session["user_id"])
    except files_client.FilesServiceError:
        app.logger.exception("files-service недоступен")
        return "Сервис временно недоступен, попробуйте позже.", 503

    if not subjects:
        return redirect(url_for("edit_subjects"))

    return render_template("main.html")


register_routes(app, "web", {
    "main": main,
})
