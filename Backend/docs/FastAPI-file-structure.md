# FastAPI File Structure

-will be altered-

the `main.py` will only hold the uvicorn run for easier runs in the future. the juice will be in the app directory, in the `app.py` file we will have the main logic of the api and the `app` instance. in the `database.py` we will have the database connection logic. in the `models.py` file we will have the database table structures. in the `schemas.py` file we will have the pydantic models.

```bash
backend/
├─ app/
│  ├─ app.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
├─ docs/
├─ .env
├─ .gitignore
├─ main.py

```

more to come
