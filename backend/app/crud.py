from sqlalchemy.orm import Session
from . import models, schemas

def list_todos(db: Session):
    return db.query(models.Todo).order_by(models.Todo.id.desc()).all()

def create_todo(db: Session, data: schemas.TodoCreate):
    todo = models.Todo(text=data.text)
    db.add(todo); db.commit(); db.refresh(todo)
    return todo

def update_todo(db: Session, todo_id: int, data: schemas.TodoUpdate):
    todo = db.get(models.Todo, todo_id)
    if not todo: return None
    if data.text is not None: todo.text = data.text
    if data.done is not None: todo.done = data.done
    db.commit(); db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.get(models.Todo, todo_id)
    if not todo: return False
    db.delete(todo); db.commit()
    return True
