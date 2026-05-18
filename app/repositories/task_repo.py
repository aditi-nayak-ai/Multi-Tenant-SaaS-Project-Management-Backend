from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.project import Project


class TaskRepository:

    def create_task(self, db: Session, task_data: dict):

        task = Task(**task_data)

        db.add(task)
        db.commit()
        db.refresh(task)

        return task


    def get_task_by_id(self, db: Session, task_id: int):

        return db.query(Task)\
            .filter(Task.id == task_id)\
            .first()


    def get_tasks_by_project(self, db: Session, project_id: int):

        return db.query(Task)\
            .filter(Task.project_id == project_id)\
            .all()


    def get_tasks_by_organization(self, db: Session, organization_id: int, page: int = 1):

        limit = 20
        offset = (page - 1) * limit

        return db.query(Task)\
            .join(Project)\
            .filter(Project.organization_id == organization_id)\
            .limit(limit)\
            .offset(offset)\
            .all()


    def update_task(self, db: Session, task_id: int, update_data: dict):

        task = db.query(Task)\
            .filter(Task.id == task_id)\
            .first()

        if not task:
            return None

        for key, value in update_data.items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)

        return task


    def delete_task(self, db: Session, task_id: int):

        task = db.query(Task)\
            .filter(Task.id == task_id)\
            .first()

        if not task:
            return None

        db.delete(task)
        db.commit()

        return task
