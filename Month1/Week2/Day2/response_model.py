#3. Create a UserRead model that adds an id: int field. Use response_model=UserRead on the route so the response always includes an id.
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
class UserCreate(BaseModel):
    name: str
    email:str
    age: int

class UserRead(BaseModel):
    id:int
    name:str
    email:str

@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "age": user.age  
    }