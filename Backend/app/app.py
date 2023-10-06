import psycopg2

from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db

from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/test")
def test(db: Session = Depends(get_db)):
    data = db.query(models.Todo).all()
    return {"data": data}


@app.get("/todos")
def get_all(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    if not todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No todos found"
        )
    return {"status": status.HTTP_200_OK, "data": todos}


@app.get("/todos/{id}", tags=["todo"])
def get_one(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )
    return {"status": status.HTTP_200_OK, "data": todo}


@app.post("/todos", tags=["todo"])
def create_todo(request: schemas.Todo, db: Session = Depends(get_db)):
    new_todo = models.Todo(**request.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return {"status": status.HTTP_201_CREATED, "data": new_todo}


@app.delete("/todos/{id}", tags=["todo"])
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)

    if todo.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found"
        )

    todo.delete(synchronize_session=False)
    db.commit()

    return {"status": status.HTTP_200_OK, "data": f"Deleted todo with id {id}"}
