from pydantic import BaseModel, EmailStr
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    done: bool = False
    description: str | None = None


class TodoCreate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int
    created_at: datetime

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
