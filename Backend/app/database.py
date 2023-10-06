import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

POSTGRES_PASSWORD = os.getenv("DATABASE_PASSWORD")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost/todo-fastapi"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
