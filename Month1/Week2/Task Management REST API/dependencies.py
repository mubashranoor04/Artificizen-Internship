from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from security import decode_access_token

# Used to read Bearer tokens from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Authentication Dependency
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    username = payload.get("sub")

    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user