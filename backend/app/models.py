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
