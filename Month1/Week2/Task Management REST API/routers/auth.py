from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import User
from schemas import UserCreate, UserLogin, Token
from security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    existing_email = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
    }


@router.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if (
        db_user is None
        or
        not verify_password(
            user.password,
            db_user.hashed_password,
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }