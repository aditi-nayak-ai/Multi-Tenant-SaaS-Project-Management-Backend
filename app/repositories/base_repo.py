from sqlalchemy.orm import Session


class BaseRepository:

    def create(self, db: Session, model):
        db.add(model)
        db.commit()
        db.refresh(model)
        return model


    def delete(self, db: Session, model):
        db.delete(model)
        db.commit()
