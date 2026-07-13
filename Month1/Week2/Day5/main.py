from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# Import Routers
from routers.users import router as users_router
from routers.auth import router as auth_router

# Lifespan Events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")
    yield
    print("Application Stopped")


app = FastAPI(
    title="Day 5 FastAPI Demo",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("=" * 40)
    print(f"Method : {request.method}")
    print(f"Path   : {request.url.path}")

    response = await call_next(request)

    print(f"Status : {response.status_code}")
    print("=" * 40)

    return response

# Global HTTPException Handler
@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "detail": exc.detail,
            "status": exc.status_code,
        },
    )
# Custom Exception
class DuplicateEmailException(Exception):
    def __init__(self):
        self.message = "Email already exists"
# Custom Exception Handler
@app.exception_handler(DuplicateEmailException)
async def duplicate_email_handler(
    request: Request,
    exc: DuplicateEmailException
):
    return JSONResponse(
        status_code=409,
        content={
            "error": True,
            "detail": exc.message,
            "status": 409,
        },
    )
# Include Routers
app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)
# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "FastAPI Day 5 Complete"
    }