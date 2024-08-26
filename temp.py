from fastapi import FastAPI,Form
from fastapi.responses import FileResponse
from enum import Enum
from pydantic import BaseModel

# class Status(Enum):
#     TO_DO = "to_do"
#     IN_PROGRESS = "in_progress"
#     DONE = "done"

# class Task(BaseModel):
#     title: str
#     status: Status

app = FastAPI()

@app.get('/')
def index():

    return FileResponse("image-512x512.jpg")

@app.get('/img')
def index():

    return FileResponse("image-512x512.jpg")