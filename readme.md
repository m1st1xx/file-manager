# 📁 Учебные файлы

<p align="center">
  <b>Персональное облачное хранилище для учебных материалов</b>
</p>

<p align="center">
  Храните лекции, лабораторные работы, отчёты, исходный код и другие учебные файлы в одном месте.
</p>

<p align="center">
  <a href="https://github.com/m1st1xx/file-manager">
    <img src="https://img.shields.io/github/stars/m1st1xx/file-manager?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/m1st1xx/file-manager">
    <img src="https://img.shields.io/github/license/m1st1xx/file-manager?style=for-the-badge" alt="License">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" alt="Docker">
</p>

---

## ✨ О проекте

**Учебные файлы** — это веб-файловый менеджер, созданный специально для хранения и организации учебных материалов.

Проект позволяет каждому пользователю создать собственную структуру предметов и хранить связанные с ними файлы в одном месте.

В отличие от обычного файлового хранилища, структура проекта ориентирована именно на учебный процесс:

```text
👤 Пользователь
│
├── 📚 Предмет 1
│   ├── 📄 Лекции
│   ├── 📄 Лабораторные работы
│   └── 💻 Код
│
├── 📚 Предмет 2
│   ├── 📄 Отчёты
│   └── 📄 Методички
│
└── 📚 Предмет 3
    └── 📄 Другие материалы
```

Каждый пользователь самостоятельно определяет список своих предметов.

Это позволяет использовать приложение студентам разных курсов, специальностей и учебных групп.

---

# 🚀 Возможности

### 👤 Пользователи

- регистрация нового аккаунта;
- вход по имени пользователя и паролю;
- вход старым способом;
- возможность перейти со старой системы авторизации на новую;
- восстановление пароля;
- персональное файловое пространство;
- изоляция файлов пользователей.

### 📚 Предметы

- добавление собственных предметов;
- удаление предметов;
- изменение списка предметов;
- индивидуальная структура для каждого пользователя;
- отсутствие заранее заданного списка дисциплин.

### 📁 Работа с файлами

- загрузка файлов;
- скачивание файлов;
- просмотр файлов по предметам;
- удаление файлов;
- разделение файлов по предметам;
- персональное хранилище для каждого пользователя.

### 🔐 Безопасность

- хеширование паролей;
- авторизация пользователей;
- изоляция пользовательских данных;
- серверная проверка данных;
- ограничение допустимых операций с файлами.

### 🎨 Интерфейс

- современный тёмный дизайн;
- адаптивный интерфейс;
- минималистичная навигация;
- удобная работа с файлами;
- отдельные страницы авторизации и регистрации.

---

# 🤖 Telegram-бот

Веб-приложение работает совместно с отдельным Telegram-ботом:

## [📱 file-manager-telegram](https://github.com/m1st1xx/file-manager-telegram)

Telegram-бот является дополнительной частью экосистемы проекта и предназначен для взаимодействия с файловым менеджером через Telegram.

Архитектура выглядит следующим образом:

```text
                    ┌─────────────────────┐
                    │       Пользователь  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   Web Interface │          │   Telegram Bot   │
       │  file-manager   │          │ file-manager-    │
       │                 │          │    telegram      │
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                └──────────────┬─────────────┘
                               │
                               ▼
                     ┌──────────────────┐
                     │  Общая файловая  │
                     │    структура     │
                     └──────────────────┘
```

Таким образом, веб-интерфейс и Telegram-бот могут использоваться как разные точки доступа к учебным материалам.

---

# 🛠 Технологии

Проект построен с использованием следующих технологий:

| Технология | Назначение |
|------------|------------|
| 🐍 **Python** | Основной язык проекта |
| 🌐 **Flask** | Backend и web-приложение |
| 🗄 **PostgreSQL** | Хранение данных пользователей |
| 🐘 **psycopg 3** | Драйвер PostgreSQL и пул соединений |
| 🔐 **Werkzeug** | Хеширование паролей |
| 🎨 **HTML / CSS / JavaScript** | Frontend |
| 🐳 **Docker** | Контейнеризация |
| 🧩 **Docker Compose** | Управление сервисами |
| ⚡ **Gunicorn** | Production WSGI-сервер |
| 🌍 **Nginx** | Reverse proxy и API-gateway микросервисов |
| 🔒 **Let's Encrypt** | HTTPS-сертификаты |
| 🤖 **aiogram** | Telegram-бот |

---

# 🏗 Архитектура

Приложение разделено на микросервисы. Каждый сервис — отдельный контейнер
с Flask + Gunicorn, владеет только своими данными и своей схемой в PostgreSQL.

```text
                    Internet
                       │
                       ▼
           Внешний Nginx (HTTPS, сеть proxy)
                       │  http://file-manager:5000
                       ▼
             gateway (nginx + /static)
         ┌─────────────┼──────────────┐
         ▼             ▼              ▼
   auth-service    web-service    files-service ──► uploads/
         │             │              ▲    │
         │             └─ /internal ──┤    │
         └──────────── /internal ─────┘    │
         │                                 │
         ▼                                 ▼
   PostgreSQL: схема auth           PostgreSQL: схема files
```

| Сервис | Отвечает за | Маршруты | Данные |
|--------|-------------|----------|--------|
| **gateway** | единая точка входа, раздача статики | все | — |
| **auth-service** | регистрация, вход, старый вход, выбор имени пользователя, сброс пароля, выход | `/`, `/register`, `/login`, `/old_login`, `/set_username`, `/reset_password`, `/logout` | `auth.users`, `auth.legacy_users`, `auth.legacy_subjects` |
| **web-service** | главная страница | `/main` | — |
| **files-service** | предметы, загрузка, скачивание и удаление файлов | `/subjects…`, `/upload…`, `/download…`, `/delete_file/…` | `files.storages`, `files.subjects`, папка `uploads/` |
| **migrate** | однократный перенос данных из SQLite | — | — |
| **postgres** | база данных | — | `/var/private/postgres` |

- **Сессия** — подписанная cookie `fm_session`. Её создаёт auth-service, а остальные
  сервисы проверяют общим секретом `TOKEN`.
- **Межсервисное взаимодействие** идёт по HTTP через внутреннее API files-service
  (`/internal/*`, заголовок `X-Internal-Token`). Через gateway это API наружу не доступно.
- **Общие шаблоны.** Шаблоны в `templates/` общие. Карта всех маршрутов лежит в
  `services/common/web.py`, поэтому `url_for(...)` работает в любом сервисе.

---

# 📂 Структура проекта

```text
file-manager/
│
├── dockerfile                 # общий образ Python-сервисов
├── docker-compose.yml
├── requirements.txt
│
├── gateway/                   # nginx-gateway (контейнер file-manager:5000)
│   ├── dockerfile
│   └── nginx.conf
│
├── services/
│   ├── common/                # конфиг, БД, сессия, карта маршрутов, имена файлов
│   ├── auth/                  # auth-service  (app.py, schema.sql)
│   ├── web/                   # web-service   (app.py)
│   └── files/                 # files-service (app.py, schema.sql)
│
├── migration/
│   └── migrate_sqlite_to_postgres.py
│
├── templates/
├── static/
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# 🐳 Запуск через Docker

## Требования

Перед запуском необходимо установить:

- Docker
- Docker Compose

Проверить установку:

```bash
docker --version
docker compose version
```

---

## Клонирование

```bash
git clone https://github.com/m1st1xx/file-manager.git
cd file-manager
```

---

## Запуск

```bash
docker compose up -d --build
```

Проверить состояние контейнеров:

```bash
docker compose ps
```

Посмотреть логи:

```bash
docker compose logs -f
```

---

# ⚙️ Конфигурация

Параметры задаются в файле `.env` рядом с `docker-compose.yml`:

| Переменная | Обязательна | Описание |
|------------|-------------|----------|
| `TOKEN` | да | секрет подписи сессий (общий для всех сервисов) |
| `POSTGRES_PASSWORD` | да | пароль пользователя PostgreSQL (только латинские буквы и цифры: он подставляется в URL подключения) |
| `POSTGRES_USER` | нет | пользователь PostgreSQL (по умолчанию `filemanager`) |
| `POSTGRES_DB` | нет | имя базы (по умолчанию `filemanager`) |
| `INTERNAL_TOKEN` | нет | токен межсервисного API (по умолчанию равен `TOKEN`) |

Пример:

```dotenv
TOKEN=длинная-случайная-строка
POSTGRES_PASSWORD=LatinLettersAndDigits123
```

> ⚠️ Не добавляйте `.env` с реальными секретами в Git.

---

# 🔐 Production

```text
Internet ─► HTTPS :443 ─► внешний Nginx ─► gateway (file-manager:5000) ─► микросервисы (Gunicorn + Flask)
```

Gateway называется `file-manager` и слушает порт `5000` в сети `proxy`,
так же как раньше монолит, поэтому конфиг внешнего nginx менять не нужно.
Внешний nginx (общий для нескольких сайтов) живёт отдельно от этого репозитория;
gateway — внутренний маршрутизатор только для микросервисов file-manager, без SSL
и без публикации портов наружу.

---

# 🔁 Переход с монолита (SQLite → PostgreSQL)

При первом `docker compose up -d --build` контейнер `migrate` переносит данные из
`/var/private/users.db` и `/var/private/new_users.db` в PostgreSQL, и только после
этого запускаются сервисы. Порядок такой:

1. Пользователи из `new_users.db` сохраняют свои `id`, имена, хеши паролей, папки и
   предметы. Пароли остаются прежними.
2. Старые аккаунты из `users.db` переносятся в `auth.legacy_users`. «Вход старым
   способом» продолжает работать. Если для старого аккаунта уже выбрано имя
   пользователя, вход сразу открывает этот аккаунт.
3. В старой базе у `username` не было `UNIQUE`, поэтому могли появиться дубликаты.
   Имя сохраняет запись с наименьшим `id` (в неё и выполнялся вход). Остальные
   получают имя вида `имя_<id>`. Список переименований есть в логе и в таблице
   `public.sqlite_import`.
4. Группы (`groups`, `group_members`) не переносятся.

Перенос выполняется в одной транзакции и только один раз: при следующих запусках
`migrate` сразу завершается. Файлы в `/var/private/uploads` не трогаются.
SQLite-файлы монтируются только для чтения и остаются как резервная копия.

Перед первым запуском рекомендуется сделать копию:

```bash
cp /var/private/users.db /var/private/new_users.db /var/private/backup/
```

Посмотреть результат переноса:

```bash
docker compose logs migrate
```

> После перехода всем пользователям нужно один раз войти заново: cookie сессии
> теперь называется по-другому.

---

# 🔄 CI/CD

Проект поддерживает автоматическое обновление сервера через GitHub Actions.

После отправки изменений:

```bash
git add .
git commit -m "Update"
git push origin main
```

GitHub Actions автоматически:

1. запускает проверки;
2. подключается к серверу;
3. получает последнюю версию проекта;
4. пересобирает Docker-контейнер;
5. запускает обновлённую версию приложения.

Схема:

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    │ SSH
    ▼
Production Server
    │
    ├── git pull
    ├── docker compose build
    └── docker compose up -d
            │
            ▼
       New version 🚀
```

Это позволяет не обновлять проект вручную после каждого изменения.

---

# 💾 Хранение данных

Данные хранятся на хосте и не пропадают при пересборке контейнеров:

| Что | Где на хосте | Кто использует |
|-----|--------------|----------------|
| база PostgreSQL | `/var/private/postgres` | postgres |
| файлы пользователей | `/var/private/uploads` | files-service |
| старые SQLite-базы (только чтение) | `/var/private/users.db`, `/var/private/new_users.db` | migrate |

Резервная копия базы:

```bash
docker compose exec postgres pg_dump -U filemanager filemanager > backup.sql
```

---

# 👨‍💻 Автор

Проект разработан **m1st1xx**.

GitHub:

https://github.com/m1st1xx

Основной репозиторий:

https://github.com/m1st1xx/file-manager

Telegram-часть проекта:

https://github.com/m1st1xx/file-manager-telegram

---

# 📱 Связанные проекты

### 📁 File Manager

Основное веб-приложение:

https://github.com/m1st1xx/file-manager

### 🤖 File Manager Telegram

Telegram-бот, работающий совместно с файловым менеджером:

https://github.com/m1st1xx/file-manager-telegram

---

# 📌 Roadmap

Планы по дальнейшему развитию проекта:

- [x] Авторизация пользователей
- [x] Регистрация
- [x] Индивидуальные предметы
- [x] Загрузка файлов
- [x] Скачивание файлов
- [x] Удаление файлов
- [x] Тёмная тема
- [x] Docker
- [x] Gunicorn
- [x] Nginx
- [x] HTTPS
- [x] Telegram-интеграция
- [x] CI/CD
- [ ] Улучшение поиска по файлам
- [ ] Предпросмотр документов
- [ ] Управление профилем
- [ ] Расширенная статистика использования хранилища
- [ ] Более подробная система прав доступа

---

# ⭐ Поддержка проекта

Если проект оказался полезным, вы можете поддержать его:

⭐ Поставить Star на GitHub

🐛 Сообщить об ошибке через Issues

💡 Предложить новую функцию

🔧 Создать Pull Request

---

<p align="center">
  <b>📚 Учебные материалы всегда под рукой.</b>
</p>

<p align="center">
  Made with ❤️ and Python
</p>
