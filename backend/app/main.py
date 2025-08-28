from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from contextlib import asynccontextmanager

from .db import get_db, create_db_and_tables
from .config import settings
from . import crud, models

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="FS Template", lifespan=lifespan)

# CORS
origins = [o.strip() for o in settings.CORS_ALLOW_ORIGINS.split(",")] if settings.CORS_ALLOW_ORIGINS else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/api/todos", response_model=list[models.TodoRead])
def list_all(db: Session = Depends(get_db)):
    return crud.list_todos(db)

@app.post("/api/todos", response_model=models.TodoRead, status_code=201)
def create(data: models.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, data)

@app.patch("/api/todos/{todo_id}", response_model=models.TodoRead)
def update(todo_id: int, data: models.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id, data)
    if not todo:
        raise HTTPException(404, "Not found")
    return todo

@app.delete("/api/todos/{todo_id}", status_code=204)
def delete(todo_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_todo(db, todo_id)
    if not ok:
        raise HTTPException(404, "Not found")
