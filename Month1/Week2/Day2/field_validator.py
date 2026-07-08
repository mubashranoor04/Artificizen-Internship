#5. Add a @field_validator to reject any name that contains numbers.
from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

    @field_validator("name")
    @classmethod

    def validate_name(cls, value):
        for char in value:
            if char.isdigit():
                raise ValueError("Name cannot contain numbers.")

        return value

@app.post("/users")
def create_user(user: UserCreate):
    return user