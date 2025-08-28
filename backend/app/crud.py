from sqlmodel import Session, select
from . import models

def list_todos(db: Session):
    statement = select(models.Todo).order_by(models.Todo.id.desc())
    return db.exec(statement).all()

def create_todo(db: Session, data: models.TodoCreate):
    todo = models.Todo.model_validate(data)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, todo_id: int, data: models.TodoUpdate):
    statement = select(models.Todo).where(models.Todo.id == todo_id)
    todo = db.exec(statement).first()
    if not todo:
        return None
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    statement = select(models.Todo).where(models.Todo.id == todo_id)
    todo = db.exec(statement).first()
    if not todo:
        return False
    
    db.delete(todo)
    db.commit()
    return True
