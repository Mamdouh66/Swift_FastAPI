from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/todos",
    tags=["todo"],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.TodoResponse],
)
def get_all(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    todos = db.query(models.Todo).filter(models.Todo.user_id == current_user.id).all()
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
def get_one(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    todo = (
        db.query(models.Todo)
        .filter(models.Todo.id == id, models.Todo.user_id == current_user.id)
        .first()
    )
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
def create_todo(
    request: schemas.TodoBase,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    new_todo = models.Todo(**request.model_dump())
    new_todo.user_id = current_user.id
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
    current_user: int = Depends(oauth2.get_current_user),
):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id)
    todo = todo_query.first()

    if todo == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    if todo.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to delete this todo",
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
    current_user: int = Depends(oauth2.get_current_user),
):
    new_todo_query = db.query(models.Todo).filter(models.Todo.id == id)
    new_todo = new_todo_query.first()

    if new_todo == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    if new_todo.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to delete this todo",
        )

    new_todo.update(request.model_dump())
    db.commit()

    return new_todo
