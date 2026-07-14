# Day 5 – End-of-Week Capstone: Task Management REST API (FastAPI)

## Overview

This project is a complete **Task Management REST API** built using **FastAPI**. It combines all the concepts learned throughout the week into a single production-style backend application.

The API provides:

- Secure user registration and login
- Password hashing using Passlib (Bcrypt)
- JWT authentication
- Task CRUD operations
- User-specific task authorization
- SQLAlchemy ORM with SQLite
- Dependency Injection
- Modular routing
- Global exception handling
- CORS configuration
- Automated testing using Pytest

The objective of this capstone was to build a secure REST API from scratch while applying authentication, authorization, database relationships, dependency injection, routing, middleware, and testing in one project.

---

# Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2
- Passlib (Bcrypt)
- Python-Jose (JWT)
- Python-Multipart
- Uvicorn
- Pytest
- FastAPI TestClient
- CORSMiddleware

---

# Project Structure

```text
Task Management REST API/
│
├── routers/
│   ├── auth.py
│   └── tasks.py
│
├── tests/
│   └── test_main.py
│
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── schemas.py
├── security.py
├── tasks.db
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# File Descriptions

## database.py

Responsible for:

- Creating the SQLite engine
- Configuring SessionLocal
- Creating the SQLAlchemy Base class
- Providing the reusable `get_db()` dependency

---

## models.py

Contains SQLAlchemy ORM models.

### User Model

- id
- username
- email
- hashed_password

### Task Model

- id
- title
- description
- status
- due_date
- owner_id

Also defines the relationship between users and their tasks.

---

## schemas.py

Contains all Pydantic schemas used for request validation and API responses.

Includes:

- UserCreate
- UserLogin
- UserResponse
- TaskCreate
- TaskUpdate
- TaskResponse
- Token

---

## security.py

Implements authentication utilities.

Includes:

- Password hashing
- Password verification
- JWT creation
- JWT decoding
- Token expiration

---

## dependencies.py

Contains reusable FastAPI dependencies.

Includes:

- Database session dependency
- Current authenticated user
- JWT verification

---

## routers/auth.py

Handles authentication.

Routes include:

- Register User
- Login User

---

## routers/tasks.py

Handles task operations.

Routes include:

- Create Task
- Get All Tasks
- Get Single Task
- Update Task
- Delete Task

Only authenticated users can access their own tasks.

---

## main.py

Application entry point.

Responsible for:

- Initializing FastAPI
- Creating database tables
- Registering routers
- Configuring CORS
- Registering exception handlers

---

## tests/test_main.py

Contains automated API tests using Pytest and TestClient.

---

# Capstone Features

## 1. User Registration

### Requirement

Implement secure user registration with hashed passwords.

### Files Used

- models.py
- schemas.py
- security.py
- routers/auth.py

### What Was Implemented

- User registration endpoint
- Password hashing using Passlib
- Duplicate username/email validation
- Database insertion

### Endpoint

```http
POST /auth/register
```

### Request

```json
{
  "username": "mubashra",
  "email": "mubashra@gmail.com",
  "password": "password123"
}
```

### What I Learned

- Never store plaintext passwords.
- Password hashing protects user credentials.
- Validation should occur before saving data.

---

# 2. User Login & JWT Authentication

### Requirement

Authenticate users and generate JWT tokens.

### Files Used

- security.py
- routers/auth.py

### What Was Implemented

- Credential verification
- JWT creation
- Secure login

### Endpoint

```http
POST /auth/login
```

### Response

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### What I Learned

- JWT enables stateless authentication.
- Tokens replace server-side sessions.
- Protected endpoints verify the token before processing requests.

---

# 3. Task Model

### Requirement

Create a Task model with:

- title
- description
- status
- due_date
- owner_id

### Files Used

- models.py
- schemas.py

### What Was Implemented

Created a Task table linked to the User table through a Foreign Key.

### What I Learned

- SQLAlchemy relationships simplify querying related data.
- Foreign Keys maintain referential integrity.

---

# 4. Task CRUD Operations

### Requirement

Implement Create, Read, Update and Delete operations.

### Files Used

- routers/tasks.py

### What Was Implemented

Implemented endpoints to:

- Create Tasks
- View All Tasks
- View Individual Task
- Update Tasks
- Delete Tasks

### Create Task Endpoint

```http
POST /tasks/
```

### Request

```json
{
  "title": "Complete FastAPI Project",
  "description": "Finish capstone",
  "status": "pending",
  "due_date": "2026-07-20"
}
```

### What I Learned

- CRUD operations form the foundation of REST APIs.
- SQLAlchemy sessions manage database persistence.

---

# 5. Authorization

### Requirement

Ensure users only access their own tasks.

### Files Used

- dependencies.py
- routers/tasks.py

### What Was Implemented

Protected every task endpoint using:

```python
get_current_user()
```

Before returning any task, the API verifies:

```text
task.owner_id == current_user.id
```

If not:

```text
403 Forbidden
```

### What I Learned

Authentication identifies users.

Authorization determines what those users are allowed to access.

---

# 6. Dependency Injection

### Files Used

- database.py
- dependencies.py

### What Was Implemented

Implemented reusable dependencies for:

- Database session
- Current authenticated user

### What I Learned

Dependency Injection removes repetitive code and improves maintainability.

---

# 7. Modular Routers

### Files Used

- main.py
- routers/auth.py
- routers/tasks.py

### What Was Implemented

Separated application logic into independent routers.

```python
app.include_router(auth.router)

app.include_router(tasks.router)
```

### What I Learned

Large FastAPI projects become easier to maintain when routes are grouped by functionality.

---

# 8. CORS & Exception Handling

### Files Used

- main.py

### What Was Implemented

Configured:

- CORSMiddleware
- Global HTTPException handler

Example error response:

```json
{
  "error": true,
  "detail": "Task not found",
  "status": 404
}
```

### What I Learned

Centralized exception handling provides consistent API responses and simplifies frontend integration.

---

# 9. Automated Testing

### Files Used

- tests/test_main.py

### Tests Implemented

- User Registration
- User Login
- Unauthorized Access
- Create Task
- Retrieve Tasks

### Command

```bash
pytest -v
```

### Output

```text
=========================
5 passed
=========================
```

### What I Learned

Automated testing validates API functionality and helps prevent regressions during development.

---

# Authentication Flow

```text
Register User
      │
      ▼
Hash Password
      │
      ▼
Store in Database
      │
      ▼
Login
      │
      ▼
Verify Password
      │
      ▼
Generate JWT
      │
      ▼
Bearer Token
      │
      ▼
Protected Endpoints
```

---

# Task Authorization Flow

```text
Request
   │
   ▼
JWT Verification
   │
   ▼
Current User
   │
   ▼
Find Task
   │
   ▼
Owner Check
   │
 ┌─┴────────────┐
 │              │
Yes            No
 │              │
Access       403 Forbidden
Granted
```

---

# Testing Summary

| Test | Result |
|------|--------|
| Register User | Passed |
| Login User | Passed |
| Unauthorized Access | Passed |
| Create Task | Passed |
| Get Tasks | Passed |

---

# Key Concepts Learned

- Password Hashing
- JWT Authentication
- Authentication vs Authorization
- SQLAlchemy Relationships
- Dependency Injection
- REST API Design
- Modular Routing
- Database Sessions
- CRUD Operations
- Automated Testing
- CORS
- Exception Handling

---

# Summary

By completing this capstone, I successfully developed a complete Task Management REST API using FastAPI. The project integrates secure user authentication with hashed passwords and JWT, SQLAlchemy ORM with SQLite, modular routers, dependency injection, protected CRUD operations, server-side authorization, CORS configuration, centralized exception handling, and automated API testing using Pytest. This project strengthened my understanding of how production-ready FastAPI applications are designed, structured, tested, and secured.