from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


####### --User schemas-- #######
class UserBase(BaseModel):
    email: EmailStr
    phone_number: PhoneNumber
    password: str


# NOTE don't return password
class UserResponse(BaseModel):
    email: EmailStr
    phone_number: PhoneNumber
    id: int
    created_at: datetime

    class config:
        orm_mode = True


####### --end of User schemas-- #######


####### --Todo schemas-- #######
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
    user: UserResponse

    class config:
        orm_mode = True


####### --end of Todo schemas-- #######


####### --Token schemas-- #######
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int


####### --end of Token schemas-- #######
