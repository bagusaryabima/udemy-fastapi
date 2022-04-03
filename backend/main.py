from fastapi import FastAPI

from backend.core.config import PROJECT_TITLE, PROJECT_VERSION


app = FastAPI(title=PROJECT_TITLE, version=PROJECT_VERSION)


@app.get("/")
def hello_world():
    return {"detail": "Hello, World!"}
