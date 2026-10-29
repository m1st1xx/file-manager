import os
import re
import unicodedata

# Символы, запрещённые в именах файлов (Windows + разделители путей)
_FORBIDDEN_RE = re.compile(r'[<>:"/\\|?*]')
_WINDOWS_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
MAX_NAME_BYTES = 255


def safe_filename(filename):
    """Безопасное имя файла с сохранением кириллицы и других не-ASCII символов.

    werkzeug.secure_filename выбрасывает все не-ASCII символы, поэтому
    «Лекция 1.pdf» превращалось в «1.pdf», а «Отчёт.docx» — в «docx».
    Здесь убираются только опасные части: путь, управляющие и запрещённые
    символы, точки/пробелы по краям. Возвращает None, если имя пустое.
    """
    if not filename:
        return None

    filename = unicodedata.normalize("NFC", filename)
    # Некоторые браузеры присылают полный путь (C:\Users\...\file.txt)
    filename = re.split(r"[/\\]", filename)[-1]
    filename = "".join(ch for ch in filename if unicodedata.category(ch)[0] != "C")
    filename = _FORBIDDEN_RE.sub("_", filename)
    filename = " ".join(filename.split()).strip(" .")

    if not filename:
        return None

    stem, ext = os.path.splitext(filename)
    if stem.upper() in _WINDOWS_RESERVED:
        filename = f"_{filename}"
        stem = f"_{stem}"

    # Ограничение длины имени в байтах (ext4: 255), расширение сохраняем
    if len(filename.encode("utf-8")) > MAX_NAME_BYTES:
        ext_bytes = len(ext.encode("utf-8"))
        if ext_bytes > 32:
            stem, ext = filename, ""
            ext_bytes = 0
        stem = stem.encode("utf-8")[: MAX_NAME_BYTES - ext_bytes].decode("utf-8", "ignore").rstrip(" .")
        filename = stem + ext

    return filename or None


def unique_filename(directory, filename):
    """Не перезаписывать существующий файл: «file.pdf» -> «file (1).pdf»."""
    if not os.path.exists(os.path.join(directory, filename)):
        return filename

    stem, ext = os.path.splitext(filename)
    counter = 1
    while True:
        candidate = f"{stem} ({counter}){ext}"
        if not os.path.exists(os.path.join(directory, candidate)):
            return candidate
        counter += 1
