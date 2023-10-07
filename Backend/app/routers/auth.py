from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, hashing
from ..database import get_db

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post(
    path="/",
    status_code=status.HTTP_200_OK,
)
def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid credentials",
        )

    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid credentials",
        )

    # Create jwt token

    # return token
    return {"token": "example"}
