#6. Create both ItemCreate and ItemRead schemas for a product (name, price, in_stock). 
# The read schema adds created_at. Use response_model to ensure created_at always appears in responses.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

class ItemRead(BaseModel):
    name: str
    price: float
    in_stock: bool
    created_at: str

@app.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate):
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "created_at": "2026-07-08 18:20:00"
    }