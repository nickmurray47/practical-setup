from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session
from .db import get_db
from .models import User
from typing import Optional

security = HTTPBearer()

# Mock user for demo purposes - replace with real auth in interviews
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """Get current user from token - mock implementation for interviews"""
    # This is a placeholder - implement real JWT validation in interviews
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    
    # Mock user for demo - replace with real user lookup
    return User(id=1, username="demo_user", email="demo@example.com")

# Optional dependency for protected routes
def require_auth(user: User = Depends(get_current_user)) -> User:
    """Require authentication for protected routes"""
    return user 