from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    done: bool = False
    description: str | None = None


class TodoCreate(TodoBase):
    pass


class TodoResponse(BaseModel):
    title: str
    done: bool
    description: str

    class config:
        orm_mode = True
