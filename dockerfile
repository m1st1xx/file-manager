# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости ОС (на всякий случай)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . .

# Создаём папку для загрузок (на случай, если её нет)
RUN mkdir -p uploads

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
