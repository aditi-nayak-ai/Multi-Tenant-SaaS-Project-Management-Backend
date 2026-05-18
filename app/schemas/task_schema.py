from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    status: TaskStatus = TaskStatus.todo
    deadline: datetime
    project_id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    status: TaskStatus | None = None
    deadline: datetime | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    project_id: int

    model_config = {"from_attributes": True}