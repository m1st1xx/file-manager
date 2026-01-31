from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    group_number: str
    hashed_password: str
    storage_path: str  # например: "uploads/Иван_Иванов"