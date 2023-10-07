from fastapi import FastAPI

from .database import engine
from .routers import todo, user, auth

from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)
