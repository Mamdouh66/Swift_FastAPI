from fastapi import FastAPI
from .schemas import TodoBase

app = FastAPI()

@app.get("/todo", tags=["todo"])
async def get_todos():
    ...