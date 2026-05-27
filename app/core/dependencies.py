from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
 
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
 
def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    """
    Resolves the authenticated user from request.state (set by TenantMiddleware).
    Raises 401 if no user is attached to the request.
    """
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
 
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
 
    return user
 
 
def require_role(*roles: str):
    """
    RBAC dependency factory.
    Usage: Depends(require_role("admin", "member"))
    """
    def _guard(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Required roles: {list(roles)}"
            )
        return current_user
    return _guard
 
