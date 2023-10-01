from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    done: bool
    description: str | None = None


class Todo(TodoBase):
    class config:
        orm_mode = True
