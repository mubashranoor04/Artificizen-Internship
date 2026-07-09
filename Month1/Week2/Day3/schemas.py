from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)