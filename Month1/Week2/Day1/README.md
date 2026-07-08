# Week 2 - Day 1: FastAPI Basics & Setup

## Overview

This project is part of my **Artificizen Internship** training program. The objective of Day 1 was to learn the fundamentals of FastAPI, understand how APIs work, create endpoints, handle requests and responses, use path and query parameters, work with HTTP status codes and exceptions, and explore FastAPI's built-in API documentation.

---

## Learning Objectives

* Understand what FastAPI is and why it is used.
* Set up a FastAPI development environment.
* Create a FastAPI application.
* Run the application using Uvicorn.
* Create GET and POST endpoints.
* Work with path parameters.
* Work with query parameters.
* Handle errors using `HTTPException`.
* Return appropriate HTTP status codes.
* Explore the automatically generated Swagger UI and ReDoc documentation.

---

## Technologies Used

* Python 3.13.6
* FastAPI 0.139.0
* Uvicorn 0.50.2
---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mubashranoor04/Artificizen-Internship.git
```

### 2. Navigate to the project

```bash
cd Month1/Week2/Day1
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI server

```bash
uvicorn main:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Practice Questions

## Practice Question 1

### Task

Create a FastAPI application with a GET `/` endpoint that returns:

```json
{
    "message": "Hello, Artificizen"
}
```

### Endpoint

```
GET /
```

### Output

```json
{
    "message": "Hello, Artificizen"
}
```

---

## Practice Question 2

### Task

Create a GET `/users/{user_id}` endpoint that accepts an integer path parameter.

### Endpoint

```
GET /users/{user_id}
```

### Successful Request

```
GET /users/25
```

Output

```json
{
    "user_id": 25
}
```

### Invalid User ID (>100)

```
GET /users/150
```

Output

```json
{
    "detail": "User not found"
}
```

Status Code

```
404 Not Found
```

### Invalid Data Type

```
GET /users/abc
```

Output

```json
{
    "detail": [
        {
            "type": "int_parsing",
            "loc": [
                "path",
                "user_id"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "abc"
        }
    ]
}
```

Status Code

```
422 Unprocessable Entity
```

---

## Practice Question 3

### Task

Create a GET `/items` endpoint with optional query parameters:

* skip (default = 0)
* limit (default = 10)

### Endpoint

```
GET /items
```

### Default Request

```
GET /items
```

Output

```json
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
```

### Using Query Parameters

```
GET /items?skip=2&limit=3
```

Output

```json
{
    "skip": 2,
    "limit": 3,
    "items": [
        "Earrings",
        "Rings",
        "Hair Tools"
    ]
}
```

---

## Practice Question 4

### Task

Raise an `HTTPException` with status code **404** whenever the requested user ID is greater than **100**.

Implemented inside the `/users/{user_id}` endpoint.

---

## Practice Question 5

### Task

Create a POST `/ping` endpoint that returns status code **201**.

### Endpoint

```
POST /ping
```

Output

```json
{
    "status": "created"
}
```

Status Code

```
201 Created
```

---

## Practice Question 6

### Task

Explore FastAPI's automatically generated documentation.

Completed by testing every endpoint through:

* Swagger UI (`/docs`)
* ReDoc (`/redoc`)

No external client (such as Postman) was required.

---

## Concepts Learned

* FastAPI application creation
* Routing
* GET requests
* POST requests
* Path parameters
* Query parameters
* JSON responses
* HTTP status codes
* Exception handling with `HTTPException`
* Automatic request validation
* Swagger UI
* ReDoc
* Uvicorn development server

---

## Screenshots

The `Screenshots` folder contains images demonstrating:

* Home endpoint (`/`)
* User endpoint (`/users/{user_id}`)
* Items endpoint (`/items`)
* Swagger UI (`/docs`)
* ReDoc (`/redoc`)
* POST `/ping` endpoint
* Error responses (404 and 422)

---

## Author

**Mubashra Noor**

Artificizen Internship — Month 1, Week 2, Day 1

FastAPI Basics & Setup

