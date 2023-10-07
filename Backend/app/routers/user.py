from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, hashing
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse,
)
def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    request.password = hashing.Hash.bcrypt(request.password)
    new_user = models.User(**request.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.UserResponse,
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )

    return user
