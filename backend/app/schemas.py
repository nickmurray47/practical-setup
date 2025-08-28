from pydantic import BaseModel
from typing import Union

class TodoBase(BaseModel):
    text: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    done: Union[bool, None] = None
    text: Union[str, None] = None

class TodoRead(TodoBase):
    id: int
    done: bool
    class Config:
        from_attributes = True
