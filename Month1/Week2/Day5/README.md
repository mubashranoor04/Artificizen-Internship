Day 5 – Routers, Middleware, Error Handling & Testing (FastAPI)
Overview

This project demonstrates how to organize a FastAPI application into modular routers, configure middleware for request processing, enable secure Cross-Origin Resource Sharing (CORS), implement centralized exception handling, execute background tasks asynchronously, manage application startup and shutdown events using lifespan handlers, and write automated API tests using Pytest and TestClient. During this practice, I learned how to structure production-ready FastAPI applications by separating concerns across multiple files while improving maintainability, debugging, and overall application reliability.

Technologies Used
Python
FastAPI
Pytest
HTTPX
FastAPI TestClient
CORSMiddleware
JSONResponse
BackgroundTasks
Project Structure
fastapi_sqlalchemy_day3/Day5/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── dependencies.py
│
├── routers/
│   ├── users.py
│   └── auth.py
│
├── tests/
│   └── test_main.py
│
├── pytest.ini
└── README.md
Files Description
main.py

Acts as the central FastAPI application. It initializes the application, registers routers, configures middleware, enables CORS, defines lifespan events, and implements global exception handlers.

routers/users.py

Contains all user-related endpoints including retrieving users, creating users, deleting users, duplicate email validation, and background task execution for welcome emails.

routers/auth.py

Contains authentication-related routes including login, registration, and protected endpoints demonstrating dependency-based authorization.

tests/test_main.py

Contains automated API tests using FastAPI's TestClient and Pytest to verify endpoint behavior, status codes, authentication, and duplicate validation.

pytest.ini

Configures Pytest to correctly locate the project root and execute all tests inside the tests directory.

Practice Question 1
Question

Split your app into at least two routers: routers/users.py and routers/auth.py. Register both in main.py with appropriate prefixes and tags.

Files Used
main.py
routers/users.py
routers/auth.py
What was implemented
Created separate APIRouter instances for user and authentication endpoints.
Registered both routers using include_router().
Assigned URL prefixes to logically group related endpoints.
Added descriptive tags for automatic grouping inside Swagger UI.
Example
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
What I Learned
Separating application logic into modular router files.
Organizing endpoints into meaningful URL prefixes.
Using tags to improve Swagger documentation readability.
Keeping main.py clean and maintainable.
Practice Question 2
Question

Add a middleware that logs every request method, path, and response status code to the console.

Files Used
main.py
What was implemented
Created a custom HTTP middleware.
Logged every incoming request method.
Logged requested URL paths.
Logged outgoing response status codes before returning responses.
Example Output
Method : GET
Path   : /users
Status : 200
What I Learned
Middleware executes before and after every request.
Logging requests greatly simplifies debugging.
Middleware provides a centralized location for cross-cutting concerns.
Practice Question 3
Question

Add CORSMiddleware configured to allow requests from http://localhost:3000 only.

Files Used
main.py
What was implemented
Added FastAPI's CORSMiddleware.
Allowed requests exclusively from a React frontend running on localhost.
Enabled credentials, headers, and all HTTP methods.
Example
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
What I Learned
Browsers restrict requests between different origins.
CORS safely enables communication between frontend and backend applications.
Restricting allowed origins improves application security.
Practice Question 4
Question

Write a global exception handler for HTTPException that always returns JSON in the shape

{
    "error": true,
    "detail": "...",
    "status": 404
}

instead of FastAPI's default response.

Files Used
main.py
What was implemented
Registered a global HTTPException handler.
Returned consistent JSON structures for all application errors.
Simplified frontend error handling through standardized responses.
Example
{
    "error": true,
    "detail": "User not found",
    "status": 404
}
What I Learned
Global exception handlers eliminate repetitive error responses.
Consistent API responses improve frontend integration.
FastAPI allows overriding default exception formatting.
Practice Question 5
Question

Add a background task to the POST /users route that "sends a welcome email" (prints a message) without blocking the response.

Files Used
routers/users.py
What was implemented
Created a reusable background function.
Used BackgroundTasks to execute the task asynchronously.
Returned API responses immediately while executing email logic afterward.
Request
POST /users
{
    "name": "Mubashra",
    "email": "mubashranoor04@gmail.com"
}
Response
{
    "message": "User created successfully",
    "user": {
        "name": "Mubashra",
        "email": "mubashranoor04@gmail.com"
    }
}
Console Output
Welcome email sent to mubashranoor04@gmail.com
What I Learned
BackgroundTasks execute after the response has been sent.
Long-running operations should not block client responses.
Background processing improves application responsiveness.
Practice Question 6
Question

Write at least three Pytest tests using TestClient:

Successful user creation
Duplicate email conflict
Protected route returning 401 without a token
Files Used
tests/test_main.py
What was implemented
Created automated endpoint tests using TestClient.
Verified successful user creation.
Tested duplicate email conflict responses.
Verified unauthorized access to protected routes.
Validated login and user retrieval endpoints.
Example Test
def test_create_user():

    response = client.post(
        "/users/",
        json={
            "name": "Mubashra",
            "email": "mubashranoor04@gmail.com"
        }
    )

    assert response.status_code == 201
Example Command
pytest -v
What I Learned
Automated testing ensures endpoints behave consistently.
TestClient simulates HTTP requests without starting a live server.
Assertions validate both status codes and response bodies.
Additional Concepts Learned
Custom Exception Classes

Instead of repeatedly raising generic HTTP exceptions, custom exception classes allow applications to represent domain-specific errors while centralizing their handling.

Lifespan Events

FastAPI's lifespan handler executes startup and shutdown logic for initializing or cleaning resources such as database pools, cache systems, or external services.

Example:

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")
    yield
    print("Application Stopped")
Request Lifecycle

Every request follows the sequence:

Client
      ↓
CORS Middleware
      ↓
Logging Middleware
      ↓
Router
      ↓
Exception Handler (if required)
      ↓
Response

Understanding this lifecycle helped clarify how middleware and exception handlers interact before responses are returned to clients.

Summary

By completing Day 5, I learned how to organize FastAPI applications into modular router files, configure middleware for logging and request processing, enable secure CORS communication between frontend and backend applications, implement centralized exception handling with consistent JSON responses, execute asynchronous background tasks, manage application startup and shutdown using lifespan events, and write automated API tests using Pytest and TestClient. These concepts collectively introduced production-level application organization and testing practices that improve scalability, maintainability, and reliability in FastAPI projects.