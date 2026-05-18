from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.project_service import ProjectService
from app.schemas.project_schema import ProjectCreate

router = APIRouter(tags=["Projects"])
project_service = ProjectService()

@router.post("/")
def create_project(request: Request, data: ProjectCreate, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return project_service.create_project(db, data.name, org_id)

@router.get("/")
def get_projects(request: Request, db: Session = Depends(get_db)):
    org_id = request.state.organization_id
    if not org_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return project_service.get_projects(db, org_id)
