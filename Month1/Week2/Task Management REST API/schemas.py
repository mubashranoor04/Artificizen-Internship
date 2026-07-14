from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict

#User Schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

#Task Schemas
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"
    due_date: Optional[date] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[date] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    due_date: Optional[date]
    owner_id: int

    model_config = ConfigDict(from_attributes=True)