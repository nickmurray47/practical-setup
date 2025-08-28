from sqlmodel import SQLModel, Field
from typing import Optional

class TodoBase(SQLModel):
    text: str

class Todo(TodoBase, table=True):
    __tablename__ = "todos"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    done: bool = Field(default=False)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(SQLModel):
    text: Optional[str] = None
    done: Optional[bool] = None

class TodoRead(TodoBase):
    id: int
    done: bool

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field(default="")
    is_active: bool = Field(default=True)
