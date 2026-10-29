import threading

import psycopg
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from .config import DATABASE_URL

_pool = None
_pool_lock = threading.Lock()


def get_pool():
    # Пул создаётся лениво, уже внутри воркера gunicorn (после fork)
    global _pool
    if _pool is None:
        with _pool_lock:
            if _pool is None:
                _pool = ConnectionPool(
                    DATABASE_URL,
                    min_size=1,
                    max_size=10,
                    kwargs={"row_factory": dict_row},
                    open=True,
                )
    return _pool


def connection():
    """Соединение из пула. В блоке with транзакция коммитится при выходе
    и откатывается при исключении."""
    return get_pool().connection()


def init_schema(sql):
    """Создание схемы сервиса. Advisory lock не даёт нескольким воркерам
    gunicorn одновременно выполнять DDL."""
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("SELECT pg_advisory_xact_lock(724501)")
        conn.execute(sql)
