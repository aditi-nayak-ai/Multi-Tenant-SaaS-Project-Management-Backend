from sqlalchemy.orm import Session
from app.models.project import Project


class ProjectRepository:

    def create_project(self, db: Session, name: str, organization_id: int):
        # organization_id comes from JWT token only, never from request body
        project = Project(name=name, organization_id=organization_id)
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    def get_project_by_id(self, db: Session, project_id: int, organization_id: int):
        # org filter prevents fetching another tenant's project by ID
        return db.query(Project)\
            .filter(
                Project.id == project_id,
                Project.organization_id == organization_id
            ).first()

    def get_projects_by_organization(self, db: Session, organization_id: int):
        return db.query(Project)\
            .filter(Project.organization_id == organization_id)\
            .all()

    def update_project(self, db: Session, project_id: int, organization_id: int, update_data: dict):
        # org filter added — can't update another tenant's project
        project = db.query(Project)\
            .filter(
                Project.id == project_id,
                Project.organization_id == organization_id
            ).first()
        if not project:
            return None
        for key, value in update_data.items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
        return project

    def delete_project(self, db: Session, project_id: int, organization_id: int):
        # org filter added — can't delete another tenant's project
        project = db.query(Project)\
            .filter(
                Project.id == project_id,
                Project.organization_id == organization_id
            ).first()
        if not project:
            return None
        db.delete(project)
        db.commit()
        return project
