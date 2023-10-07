from fastapi import FastAPI

from .database import engine, get_db
from .routers import todo, user

from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)
app.include_router(user.router)
