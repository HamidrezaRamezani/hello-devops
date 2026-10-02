import os

from fastapi import FastAPI

app = FastAPI()
VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def hello():
    return {"message": "Hello from hello-devops v2", "version": VERSION}
