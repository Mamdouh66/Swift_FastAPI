from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db

from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/todo", tags=["todo"], response_model=List[schemas.Todo])
def get_all(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos


@app.post("/todo", tags=["todo"])
def create_todo(request: schemas.TodoBase, db: Session = Depends(get_db)):
    new_todo = models.Todo(
        title=request.title, done=request.done, description=request.description
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
