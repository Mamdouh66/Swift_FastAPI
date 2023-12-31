from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import todo, user, auth


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"data": "Hello, this is root"}
