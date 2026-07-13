# Day 5 – Routers, Middleware, Error Handling & Testing (FastAPI)

## Overview

This project demonstrates how to organize a FastAPI application into modular components using routers, middleware, exception handlers, background tasks, lifespan events, and automated testing. The goal of this practice was to learn how production-level FastAPI applications are structured, making the codebase easier to maintain, extend, and test.

By completing this practice, I learned how to:

- Split a FastAPI application into multiple routers.
- Register routers using `include_router()`.
- Configure middleware for request logging.
- Enable Cross-Origin Resource Sharing (CORS).
- Create global exception handlers.
- Implement custom exception classes.
- Execute background tasks without blocking responses.
- Manage application startup and shutdown using lifespan events.
- Write automated API tests using Pytest and TestClient.

---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- FastAPI TestClient
- CORSMiddleware
- BackgroundTasks

---

# Project Structure

```text
Day5/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── dependencies.py
├── requirements.txt
├── pytest.ini
├── README.md
│
├── routers/
│   ├── auth.py
│   └── users.py
│
└── tests/
    └── test_main.py
```

---

# Files Description

## main.py

Acts as the application's entry point. It initializes the FastAPI application, registers routers, configures middleware, enables CORS, defines lifespan events, and implements global exception handling.

---

## routers/users.py

Contains all user-related routes, including creating users, retrieving users, validating duplicate email addresses, and executing background tasks.

---

## routers/auth.py

Contains authentication routes such as login and protected endpoints used to demonstrate authorization.

---

## tests/test_main.py

Contains automated API tests written using Pytest and FastAPI's TestClient.

---

## pytest.ini

Configures Pytest to correctly discover the project files and test directory.

---

# Practice Question 1

## Question

Split your application into at least two routers:

- `routers/users.py`
- `routers/auth.py`

Register both routers in `main.py` using appropriate prefixes and tags.

---

## Files Used

- `main.py`
- `routers/users.py`
- `routers/auth.py`

---

## What Was Implemented

- Created separate `APIRouter` instances.
- Moved user routes into `users.py`.
- Moved authentication routes into `auth.py`.
- Registered routers using `include_router()`.
- Added URL prefixes.
- Added Swagger documentation tags.

---

## Example

```python
app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)
```

---

## What I Learned

- How to organize large applications into multiple files.
- Why separating routes improves maintainability.
- How prefixes automatically group related endpoints.
- How tags organize Swagger documentation.

---

# Practice Question 2

## Question

Add middleware that logs every request method, request path, and response status code.

---

## Files Used

- `main.py`

---

## What Was Implemented

- Created a custom HTTP middleware.
- Logged request methods.
- Logged request paths.
- Logged response status codes.

---

## Example Console Output

```text
Method: GET
Path: /users
Status: 200
```

---

## What I Learned

- Middleware executes before and after every request.
- Middleware is useful for logging, authentication, timing, and request modification.
- Logging simplifies debugging and monitoring.

---

# Practice Question 3

## Question

Configure `CORSMiddleware` to allow requests only from:

```
http://localhost:3000
```

---

## Files Used

- `main.py`

---

## What Was Implemented

- Added FastAPI's `CORSMiddleware`.
- Allowed requests from a React frontend.
- Enabled credentials.
- Allowed all HTTP methods.
- Allowed all request headers.

---

## Example

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## What I Learned

- Browsers block requests from different origins by default.
- CORS allows trusted frontend applications to communicate with the backend.
- Restricting allowed origins improves security.

---

# Practice Question 4

## Question

Create a global exception handler that returns errors in the following format:

```json
{
    "error": true,
    "detail": "...",
    "status": 404
}
```

---

## Files Used

- `main.py`

---

## What Was Implemented

- Registered a global `HTTPException` handler.
- Returned consistent JSON responses for every API error.
- Replaced FastAPI's default error response.

---

## Example Response

```json
{
    "error": true,
    "detail": "User not found",
    "status": 404
}
```

---

## What I Learned

- Global exception handlers eliminate repeated error-handling code.
- Consistent error responses simplify frontend development.
- FastAPI allows custom formatting for exceptions.

---

# Practice Question 5

## Question

Add a background task to the `POST /users` route that sends a welcome email (prints a message) without blocking the response.

---

## Files Used

- `routers/users.py`

---

## What Was Implemented

- Created a background function.
- Used `BackgroundTasks`.
- Returned the API response immediately.
- Executed the email task after the response.

---

## Request

```http
POST /users
```

```json
{
    "name": "Mubashra",
    "email": "mubashranoor04@gmail.com"
}
```

---

## Response

```json
{
    "message": "User created successfully",
    "user": {
        "name": "Mubashra",
        "email": "mubashranoor04@gmail.com"
    }
}
```

---

## Console Output

```text
Welcome email sent to mubashranoor04@gmail.com
```

---

## What I Learned

- Background tasks run after the response is returned.
- Long-running operations should not block API responses.
- Background processing improves application performance.

---

# Practice Question 6

## Question

Write automated tests using Pytest and TestClient for:

- Successful user creation
- Duplicate email conflict
- Unauthorized protected route

---

## Files Used

- `tests/test_main.py`

---

## What Was Implemented

- Created API tests using FastAPI's `TestClient`.
- Verified successful user creation.
- Tested duplicate email validation.
- Tested unauthorized access.
- Verified login endpoint.
- Verified user retrieval endpoint.

---

## Example Test

```python
def test_create_user():

    response = client.post(
        "/users/",
        json={
            "name": "Mubashra",
            "email": "mubashranoor04@gmail.com"
        }
    )

    assert response.status_code == 201
```

---

## Running the Tests

```bash
pytest -v
```

---

## What I Learned

- Automated tests verify application behavior.
- `TestClient` simulates HTTP requests without starting the server.
- Assertions validate both status codes and response content.

---

# Additional Concepts Learned

## Custom Exception Classes

Custom exception classes allow developers to represent application-specific errors while centralizing error handling. This improves readability and keeps route logic clean.

---

## Lifespan Events

Lifespan events manage application startup and shutdown.

Example:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):

    print("Application Started")

    yield

    print("Application Stopped")
```

Typical startup tasks include:

- Database initialization
- Cache creation
- Loading machine learning models
- Opening external connections

Typical shutdown tasks include:

- Closing database connections
- Clearing cache
- Releasing external resources

---

## Request Lifecycle

Every request follows this sequence:

```text
Client
   │
   ▼
CORS Middleware
   │
   ▼
Logging Middleware
   │
   ▼
Router
   │
   ▼
Background Tasks
   │
   ▼
Exception Handler (if needed)
   │
   ▼
Response
```

Understanding this lifecycle helped clarify how middleware, routers, background tasks, and exception handlers work together inside FastAPI.

---

# Summary

By completing Day 5, I learned how to structure FastAPI applications using modular routers, configure middleware for request processing, enable CORS for frontend integration, create centralized exception handlers, execute asynchronous background tasks, manage application startup and shutdown through lifespan events, and write automated tests using Pytest and TestClient.

These concepts represent important production-level FastAPI practices that improve application organization, scalability, maintainability, and reliability.
