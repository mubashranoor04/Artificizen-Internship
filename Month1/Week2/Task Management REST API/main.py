from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from database import Base, engine
from routers import auth, tasks

# Lifespan Events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")

    # Create database tables
    Base.metadata.create_all(bind=engine)

    yield

    print("Application Stopped")

# FastAPI App
app = FastAPI(
    title="Task Management REST API",
    lifespan=lifespan
)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Global Exception Handler
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "detail": exc.detail,
            "status": exc.status_code
        }
    )
# Root Route
@app.get("/")
def root():
    return {
        "message": "Task Management REST API"
    }
# Register Routers
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)
app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)