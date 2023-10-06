# Database Connection

For database connection we will be using postgres, sqlalchemy.  
click [here](https://fastapi.tiangolo.com/tutorial/) for fastapi docs about SQL.

make sure you have a postgres driver downloaded, e.g. `psycopg2`

## database important code

in _database.py file_  
first get the requirements

```python
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

```

then define the postgres pass in env file, and define database url.

```python
load_dotenv()

POSTGRES_PASSWORD = os.getenv("DATABASE_PASSWORD")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost/todo-fastapi"
)
```

then create the engine and the session maker, and then create the Base to use later for the models

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
```

for the get_db() its used to create independent database sessions for each request, and use the session throughout the request and close it after that because of the [`yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

end of database.py file

---

for _models.py file_

import the following

```python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

```

define the class which will be turned to a db table by the ORM

```python
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    done = Column(Boolean, server_default="FALSE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False
    )

```

end of models.py file

---

in the main _app.py file_

the following are the important imports to deal with orm and db

```python
from fastapi import Depends

from sqlalchemy.orm import Session

from .database import engine, get_db

from . import models, schemas

models.Base.metadata.create_all(bind=engine)
```

and then all that needs to be done is to add it to the functions arguemnts with a dependency

```python
def example_function(db: Session = Depends(get_db)):
```
