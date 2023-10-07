from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import engine, get_db

router = APIRouter(
    prefix="/todos",
    tags=["todo"],
)


@router.get(
    path="/",
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


@router.get(
    path="/{id}",
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


@router.post(
    path="/",
    response_model=schemas.TodoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(request: schemas.TodoResponse, db: Session = Depends(get_db)):
    new_todo = models.Todo(**request.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.delete(
    path="/{id}",
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


@router.put(
    path="/{id}",
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
