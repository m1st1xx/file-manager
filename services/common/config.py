from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[2]
TEMPLATES_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"

# Общий секрет подписи cookie-сессии: одинаковый у всех сервисов,
# поэтому сессия, созданная auth-service, читается web- и files-service.
TOKEN = getenv("TOKEN")

# Токен для внутренних (межсервисных) запросов. Если отдельный не задан,
# используется TOKEN, чтобы не требовать новых переменных в .env.
INTERNAL_TOKEN = getenv("INTERNAL_TOKEN") or TOKEN

DATABASE_URL = getenv("DATABASE_URL", "postgresql://filemanager:filemanager@localhost:5432/filemanager")

FILES_SERVICE_URL = getenv("FILES_SERVICE_URL", "http://files-service:5000")

UPLOAD_BASE = getenv("UPLOAD_BASE", "uploads")
