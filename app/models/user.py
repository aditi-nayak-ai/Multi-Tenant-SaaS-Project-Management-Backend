from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)

    organization_id = Column(Integer, ForeignKey("organizations.id"))
