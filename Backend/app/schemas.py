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


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class config:
        orm_mode = True
