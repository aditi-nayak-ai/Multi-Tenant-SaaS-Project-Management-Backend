from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    organization_id = Column(Integer, ForeignKey("organizations.id"))
