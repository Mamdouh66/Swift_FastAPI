from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, schemas, hashing, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post(
    path="/",
    status_code=status.HTTP_200_OK,
)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.email == request.username).first()

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
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    # return token
    return {"token": access_token, "token_type": "bearer"}
