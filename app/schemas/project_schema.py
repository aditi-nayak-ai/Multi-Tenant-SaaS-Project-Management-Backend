from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    # organization_id removed — must come from JWT token only, never from client

class ProjectResponse(BaseModel):
    id: int
    name: str
    organization_id: int  # included in response so client knows which org it belongs to

    class Config:
        orm_mode = True
