from fastapi.testclient import TestClient
from app import app, schemas, database
from .test_db import override_get_db, engine
from ..database import get_db

database.Base.metadata.create_all(bind=engine)

app.app.dependency_overrides[get_db] = override_get_db

client = TestClient(app.app)


def test_root():
    res = client.get("/")
    assert res.json().get("data") == "Hello, this is root"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/",
        json={
            "email": "test3@tester.tst",
            "password": "test123",
            "phone_number": "+966500000004",
        },
    )
    new_user = schemas.UserResponse(**res.json())

    assert new_user.email == "test3@tester.tst"
    assert res.status_code == 201
