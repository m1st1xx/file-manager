import hmac
from functools import wraps

from flask import Flask, abort, request

from .config import INTERNAL_TOKEN, STATIC_DIR, TEMPLATES_DIR, TOKEN

# Карта всех страниц сайта: endpoint -> (правило, методы, сервис-владелец).
# Каждый сервис обрабатывает только свои маршруты, а чужие регистрирует
# как build_only, чтобы url_for(...) в общих шаблонах работал везде.
# Маршрутизацию запросов по сервисам делает gateway (gateway/nginx.conf).
ROUTES = {
    # auth-service
    "index": ("/", ["GET"], "auth"),
    "register": ("/register", ["POST"], "auth"),
    "login": ("/login", ["POST"], "auth"),
    "old_login": ("/old_login", ["POST"], "auth"),
    "set_username": ("/set_username", ["GET", "POST"], "auth"),
    "reset_password": ("/reset_password", ["GET", "POST"], "auth"),
    "logout": ("/logout", ["POST"], "auth"),
    # web-service
    "main": ("/main", ["GET"], "web"),
    # files-service
    "edit_subjects": ("/subjects", ["GET", "POST"], "files"),
    "delete_subject": ("/subjects/delete", ["POST"], "files"),
    "download_select": ("/download", ["GET"], "files"),
    "upload_select": ("/upload", ["GET"], "files"),
    "subject_files": ("/<mode>/<path:subject>", ["GET", "POST"], "files"),
    "delete_file": ("/delete_file/<path:subject>/<path:filename>", ["POST"], "files"),
    "download_file": ("/download_file/<path:subject>/<path:filename>", ["GET"], "files"),
}


def create_app(name):
    app = Flask(
        name,
        template_folder=str(TEMPLATES_DIR),
        static_folder=str(STATIC_DIR),
    )
    app.secret_key = TOKEN
    # Своё имя cookie: сессии старого монолита (где user_id мог быть id из
    # старой БД users.db) после перехода просто перестают действовать.
    app.config["SESSION_COOKIE_NAME"] = "fm_session"
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    return app


def register_routes(app, service, views):
    for endpoint, (rule, methods, owner) in ROUTES.items():
        if owner == service:
            app.add_url_rule(rule, endpoint, views[endpoint], methods=methods)
        else:
            app.add_url_rule(rule, endpoint, build_only=True)


def internal_only(view):
    """Защита внутренних эндпоинтов /internal/*: доступны только сервисам,
    знающим INTERNAL_TOKEN. Снаружи gateway их вообще не проксирует."""

    @wraps(view)
    def wrapper(*args, **kwargs):
        token = request.headers.get("X-Internal-Token", "")
        if not INTERNAL_TOKEN or not hmac.compare_digest(token, INTERNAL_TOKEN):
            abort(403)
        return view(*args, **kwargs)

    return wrapper
