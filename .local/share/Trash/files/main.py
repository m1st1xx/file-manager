import os
import shutil
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.concurrency import run_in_threadpool

from models import User
from database import engine, create_db_and_tables, get_session

# === Настройки ===
UPLOAD_DIR = Path("uploads")
SUBJECTS = ["Математика", "Физика", "Химия", "Программирование", "История"]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# === Модели запросов ===
class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    group_number: str
    password: str

# === Вспомогательные функции ===
def sanitize_name(name: str) -> str:
    # Удаляем потенциально опасные символы
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in name).strip()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def create_user_directories(first_name: str, last_name: str) -> str:
    safe_first = sanitize_name(first_name)
    safe_last = sanitize_name(last_name)
    folder_name = f"{safe_first}_{safe_last}"
    user_dir = UPLOAD_DIR / folder_name

    # Создаём корневую папку uploads, если нет
    UPLOAD_DIR.mkdir(exist_ok=True)

    # Создаём папку пользователя
    await run_in_threadpool(user_dir.mkdir, parents=True, exist_ok=False)

    # Создаём папки предметов
    for subject in SUBJECTS:
        subject_dir = user_dir / sanitize_name(subject)
        await run_in_threadpool(subject_dir.mkdir, parents=True, exist_ok=False)

    return str(user_dir)

# === FastAPI app ===
app = FastAPI(title="School File Manager")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    data: RegisterRequest,
    session: Session = Depends(get_session)
):
    # Проверка: существует ли уже такой пользователь?
    statement = select(User).where(
        User.first_name == data.first_name,
        User.last_name == data.last_name,
        User.group_number == data.group_number
    )
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь уже существует"
        )

    try:
        # Создаём директории
        storage_path = await create_user_directories(data.first_name, data.last_name)
        
        # Сохраняем в БД
        new_user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            group_number=data.group_number,
            hashed_password=hash_password(data.password),
            storage_path=storage_path
        )
        session.add(new_user)
        session.commit()
        return {"message": "Пользователь успешно зарегистрирован"}
    
    except FileExistsError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Папка пользователя уже существует"
        )
    except Exception as e:
        # Откат: удаляем папку, если БД не сохранилась
        if 'storage_path' in locals():
            shutil.rmtree(storage_path, ignore_errors=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при создании пользователя: {str(e)}"
        )
