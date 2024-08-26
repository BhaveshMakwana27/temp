from fastapi import FastAPI,Form
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

@app.get('')
def index():

    return True