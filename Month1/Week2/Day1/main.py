from fastapi import FastAPI, HTTPException

app = FastAPI()


"""
Practice Question 1:
Create a FastAPI app with a GET / route that returns:
{"message": "Hello, Artificizen"}

Output:
GET /
{
    "message": "Hello, Artificizen"
}
"""
@app.get("/")
def home():
    return {"message": "Hello, Artificizen"}


"""
Practice Question 2:
Add a GET /users/{user_id} route that returns the user ID as an integer.
If the user ID is greater than 100, return a 404 error.

Example Outputs:

GET /users/25
{
    "user_id": 25
}

GET /users/150
Status Code: 404 Not Found

{
    "detail": "User not found"
}

GET /users/abc
Status Code: 422 Unprocessable Entity

{
    "detail": [
        {
            "type": "int_parsing",
            "loc": ["path", "user_id"],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "abc"
        }
    ]
}
"""
@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id > 100:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"user_id": user_id}


"""
Practice Question 3:
Add a GET /items route with optional query parameters:
- skip (default = 0)
- limit (default = 10)

Example Outputs:

GET /items
{
    "skip": 0,
    "limit": 10,
    "items": [
        "Bag",
        "Watch",
        "Earrings",
        "Rings",
        "Hair Tools",
        "Makeup Pouch",
        "Necklace",
        "Outfit",
        "Shoes",
        "Sunnies"
    ]
}

GET /items?skip=2&limit=3
{
    "skip": 2,
    "limit": 3,
    "items": [
        "Earrings",
        "Rings",
        "Hair Tools"
    ]
}
"""
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):

    items = [
        "Bag",
        "Watch",
        "Earrings",
        "Rings",
        "Hair Tools",
        "Makeup Pouch",
        "Necklace",
        "Outfit",
        "Shoes",
        "Sunnies"
    ]

    return {
        "skip": skip,
        "limit": limit,
        "items": items[skip: skip + limit]
    }


"""
Practice Question 5:
Add a POST /ping route that returns status code 201 with:
{"status": "created"}

Output:

POST /ping
Status Code: 201 Created

{
    "status": "created"
}
"""
@app.post("/ping", status_code=201)
def ping():
    return {"status": "created"}


"""
Practice Question 6:
Explored the auto-generated API documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Verified all endpoints directly from the browser without writing any client code.
"""