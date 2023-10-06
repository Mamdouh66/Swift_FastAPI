# Pydantic schemas

One of the most important features of FastAPI is their heavy use of pydantic, the main feature of pydantic is data validation. which we will with dealing with database models, enforcing response and request models.

in _schemas.py_ file

as simple as that we can get the powerful features, firstly lets make a base schema for our project which would have the traits that we would want in every child of it. an important step is that it must extends the `BaseModel` from pydantic

for TodoResponse we will use the schema later for making a response_model inside of it we define what do we want send back to the user, here you would think we duplicated the base model but actually we just sending the necessary information without the rest that would come with the database like the id and created_at this is a simple example. Based in our needs we can put whatever in their. we must create the `config class` for letting the response_model later know that its dealing with a db instance

```python
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
```

end of _schemas.py_ file

---

now for the main _app.py_ file

the following is an example code of how can we take advantage of the pydantic schemas, as seen in the decorator we can define a response model FastAPI will use this response_model to do all the data documentation, validation, etc. and also to convert and filter the output data to its type declaration.

Also, we can define the incoming request as our pydantic schema and validate the incoming data based on how we want our schema and db model should look like

we use `**request.model_dump()` to unpack the schema parameters for creating a new todo, instead of explicitly specifying each parameter e.g. `title = request.title ...`

```python
@app.post(
    "/todos",
    tags=["todo"],
    response_model=schemas.TodoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(request: schemas.TodoResponse, db: Session = Depends(get_db)):
    new_todo = models.Todo(**request.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
```
