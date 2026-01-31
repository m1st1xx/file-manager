from sqlmodel import create_engine, SQLModel, Session
from pathlib import Path

# Создаём папку для БД, если нет
DB_PATH = Path("db.sqlite")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
