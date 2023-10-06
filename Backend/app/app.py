from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db

from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get(
    "/todos",
    tags=["todo"],
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.TodoResponse],
)
def get_all(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    if not todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No todos found"
        )
    return todos


@app.get(
    "/todos/{id}",
    tags=["todo"],
    status_code=status.HTTP_200_OK,
    response_model=schemas.TodoResponse,
)
def get_one(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )
    return todo


@app.post(
    "/todos",
    tags=["todo"],
    response_model=schemas.TodoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(request: schemas.TodoResponse, db: Session = Depends(get_db)):
    new_todo = models.Todo(**request.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.delete(
    "/todos/{id}",
    tags=["todo"],
    status_code=status.HTTP_200_OK,
    response_model=schemas.TodoResponse,
)
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)

    if todo.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    todo.delete(synchronize_session=False)
    db.commit()

    return f"Deleted todo with id {id}"


@app.put(
    "/todos/{id}",
    tags=["todo"],
    status_code=status.HTTP_200_OK,
    response_model=schemas.TodoResponse,
)
def update_todo(id: int, request: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = db.query(models.Todo).filter(models.Todo.id == id)

    if new_todo.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    new_todo.update(request.model_dump())
    db.commit()

    return new_todo.first()
