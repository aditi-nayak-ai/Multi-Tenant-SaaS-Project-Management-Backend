from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.models.organization import Organization
from app.workers.celery_worker import send_welcome_email

router = APIRouter(tags=["Organizations"])

@router.post("/")
def create_organization(name: str, db: Session = Depends(get_db)):
    organization = Organization(name=name)
    db.add(organization)
    db.commit()
    db.refresh(organization)

    # Trigger background job — non-blocking
    send_welcome_email.delay(
        org_id=organization.id,
        org_name=organization.name
    )

    return organization

@router.get("/")
def get_organizations(db: Session = Depends(get_db)):
    organizations = db.query(Organization).all()
    return organizations