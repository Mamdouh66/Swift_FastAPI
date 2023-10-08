from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
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
    response_model=schemas.TodoCreate,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(
    request: schemas.TodoBase,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    new_todo = models.Todo(**request.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.delete(
    path="/{id}",
    status_code=status.HTTP_200_OK,
)
def delete_todo(
    id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    todo = db.query(models.Todo).filter(models.Todo.id == id)

    if todo.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    todo.delete(synchronize_session=False)
    db.commit()

    return {"Data": f"Deleted todo with id {id}"}


@router.put(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.TodoResponse,
)
def update_todo(
    id: int,
    request: schemas.TodoCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    new_todo = db.query(models.Todo).filter(models.Todo.id == id)

    if new_todo.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    new_todo.update(request.model_dump())
    db.commit()

    return new_todo.first()
