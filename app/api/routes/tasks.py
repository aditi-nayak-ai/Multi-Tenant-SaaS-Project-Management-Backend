from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskCreate, TaskUpdate

router = APIRouter(tags=["Tasks"])
task_service = TaskService()

@router.post("/")
def create_task(request: Request, data: TaskCreate, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    task = task_service.create_task(db, data, org_id)
    if not task:
        raise HTTPException(status_code=404, detail="Project not found or not in your organization")
    return task

@router.get("/")
def get_tasks(request: Request, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return task_service.get_tasks(db, org_id)

@router.patch("/{task_id}")
def update_task(task_id: int, request: Request, data: TaskUpdate, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    task = task_service.update_task(db, task_id, org_id, data.model_dump(exclude_unset=True))
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, request: Request, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    result = task_service.delete_task(db, task_id, org_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result