from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Login
@router.post("/login")
def login():

    return {
        "access_token": "fake-jwt-token",
        "token_type": "bearer"
    }
# Register
@router.post("/register")
def register():

    return {
        "message": "User Registered"
    }
# Fake Authentication Dependency
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    if token != "fake-jwt-token":

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return {
        "username": "john"
    }
# Protected Route
@router.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    return current_user