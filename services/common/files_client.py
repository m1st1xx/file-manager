"""HTTP-клиент внутреннего API files-service (для auth- и web-service)."""
import requests

from .config import FILES_SERVICE_URL, INTERNAL_TOKEN

TIMEOUT = 10


class FilesServiceError(Exception):
    pass


def _request(method, path, **kwargs):
    try:
        response = requests.request(
            method,
            FILES_SERVICE_URL + path,
            headers={"X-Internal-Token": INTERNAL_TOKEN or ""},
            timeout=TIMEOUT,
            **kwargs,
        )
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        raise FilesServiceError(str(e)) from e


def create_storage(user_id, folder_path=None, subjects=None):
    """Создать хранилище пользователя. folder_path передаётся, когда нужно
    подключить уже существующую папку (перенос старого аккаунта)."""
    return _request(
        "POST",
        "/internal/storages",
        json={"user_id": user_id, "folder_path": folder_path, "subjects": subjects or []},
    )


def get_subjects(user_id):
    return _request("GET", f"/internal/users/{user_id}/subjects")["subjects"]
