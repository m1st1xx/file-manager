# Общий образ для всех Python-микросервисов (auth, web, files) и миграции.
# Какой сервис запускать, задаётся переменной SERVICE в docker-compose.yml.
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services ./services
COPY migration ./migration
COPY templates ./templates
COPY static ./static

RUN mkdir -p uploads

ENV PYTHONUNBUFFERED=1 \
    SERVICE=web

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 --workers 2 --threads 4 --timeout 120 "services.${SERVICE}.app:app"
