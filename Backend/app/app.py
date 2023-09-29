from fastapi import FastAPI
from .schemas import TodoBase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}