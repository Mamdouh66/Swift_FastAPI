from pydantic import BaseModel, EmailStr
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    done: bool = False
    description: str | None = None


class TodoCreate(TodoBase):
    user_id: int


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    user_id: int

    class config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    password: str


# NOTE don't return password
class UserResponse(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime

    class config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
