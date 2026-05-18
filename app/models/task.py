from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.core.database import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String)
    status = Column(String)

    deadline = Column(DateTime)

    project_id = Column(Integer, ForeignKey("projects.id"))
