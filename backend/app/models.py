from sqlalchemy import Boolean, Column, Integer, String
from .db import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    done = Column(Boolean, default=False)
