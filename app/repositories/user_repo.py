from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:

    def create_user(self, db: Session, user_data: dict):
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    def get_user_by_email(self, db: Session, email: str):
        return db.query(User)\
            .filter(User.email == email)\
            .first()


    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User)\
            .filter(User.id == user_id)\
            .first()


    def get_users_by_organization(self, db: Session, organization_id: int):
        return db.query(User)\
            .filter(User.organization_id == organization_id)\
            .all()


    def delete_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user
