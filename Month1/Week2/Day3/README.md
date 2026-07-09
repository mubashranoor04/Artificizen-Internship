# Day 3 - Database Integration with SQLAlchemy (FastAPI)

## Overview

This project demonstrates how to integrate SQLAlchemy with FastAPI using SQLite as the database. During this practice, I learned how to connect a FastAPI application to a database, create SQLAlchemy models, validate request and response data using Pydantic schemas, perform CRUD operations, and work with relationships using foreign keys.

---

# Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# Project Structure

```
fastapi_sqlalchemy_day3/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── users.db
└── README.md
```

---

# Files Description

## database.py

Responsible for:

- Creating the database connection
- Creating the SQLAlchemy engine
- Creating SessionLocal
- Creating the Base class
- Creating the get_db() dependency for database sessions

---

## models.py

Contains the SQLAlchemy models.

Current models:

- User
- Post

These models represent the database tables.

---

## schemas.py

Contains the Pydantic schemas.

Current schemas:

- UserCreate
- UserRead

These schemas validate incoming requests and format outgoing responses.

---

## main.py

Contains:

- FastAPI application
- API endpoints
- CRUD operations
- Dependency Injection
- Database table creation

---

# Practice Question 1

## Question

Set up SQLAlchemy with SQLite. Create a User model with id, name, email and is_active. Run Base.metadata.create_all() to create the table.

---

## Files Used

- database.py
- models.py
- main.py

---

## What was implemented

- Connected FastAPI with SQLite.
- Created SQLAlchemy engine.
- Created SessionLocal.
- Created Base using declarative_base().
- Created the User model.
- Created the users table using Base.metadata.create_all().

---

## Output

- users.db file created successfully.
- users table created inside the database.
- FastAPI server started successfully.

---

## What I Learned

- How SQLAlchemy connects to a database.
- Difference between Engine and Session.
- How Base is used by SQLAlchemy models.
- How SQLAlchemy creates tables automatically.

---

# Practice Question 2

## Question

Write a get_db dependency using yield and plug it into a POST /users route that saves a new user to the database.

---

## Files Used

- database.py
- schemas.py
- models.py
- main.py

---

## What was implemented

- Created get_db() dependency using yield.
- Added UserCreate schema.
- Added UserRead schema.
- Implemented POST /users endpoint.
- Inserted a new user into the database.

---

## Request

```json
{
    "name": "Mubashra Noor",
    "email": "mubs.noor04@gmail.com"
}
```

---

## Response

```json
{
    "id": 1,
    "name": "Mubashra Noor",
    "email": "mubs.noor04@gmail.com",
    "is_active": true
}
```

---

## What I Learned

- Why Pydantic schemas are different from SQLAlchemy models.
- How Depends(get_db) injects the database session.
- How db.add(), db.commit(), and db.refresh() work.
- How data is saved into SQLite.

---

# Practice Question 3

## Question

Write a GET /users/{user_id} route that fetches a user from the database and returns 404 if the user is not found.

---

## Files Used

- main.py

---

## What was implemented

- Implemented GET /users/{user_id}.
- Queried the database using SQLAlchemy.
- Returned HTTP 404 if the user does not exist.

---

## Request

```
GET /users/1
```

---

## Response

```json
{
    "id": 1,
    "name": "Mubashra Noor",
    "email": "mubs.noor04@gmail.com",
    "is_active": true
}
```

---

## Invalid Request

```
GET /users/999
```

---

## Response

```json
{
    "detail": "User not found"
}
```

Status Code

```
404 Not Found
```

---

## What I Learned

- How to fetch a single record from the database.
- How .filter() and .first() work.
- How to return HTTP exceptions in FastAPI.

---

# Practice Question 4

## Question

Write a GET /users route that returns all users using skip and limit query parameters.

---

## Files Used

- main.py

---

## What was implemented

- Implemented GET /users.
- Added pagination using skip and limit.
- Returned multiple users from the database.

---

## Request

```
GET /users
```

---

## Response

```json
[
    {
        "id": 1,
        "name": "Mubashra Noor",
        "email": "mubs.noor04@gmail.com",
        "is_active": true
    }
]
```

---

## Example

```
GET /users?skip=0&limit=1
```

Returns only one user.

---

## What I Learned

- How to fetch multiple records.
- How pagination works.
- Difference between .first() and .all().
- How response_model can return a list of objects.

---

# Practice Question 5

## Question

Write a DELETE /users/{user_id} route that deletes a user and returns 204 No Content.

---

## Files Used

- main.py

---

## What was implemented

- Implemented DELETE endpoint.
- Deleted the selected user.
- Returned HTTP 204 after successful deletion.

---

## Request

```
DELETE /users/1
```

---

## Response

```
204 No Content
```

---

## Invalid Request

```
DELETE /users/999
```

---

## Response

```json
{
    "detail": "User not found"
}
```

Status Code

```
404 Not Found
```

---

## What I Learned

- How db.delete() works.
- Why db.commit() is required after deleting.
- How to return proper HTTP status codes.

---

# Practice Question 6

## Question

Add a Post model with a ForeignKey to User. Create GET /users/{user_id}/posts.

---

## Files Used

- models.py
- main.py

---

## What was implemented

- Added Post model.
- Added ForeignKey.
- Added relationship() between User and Post.
- Implemented GET /users/{user_id}/posts.

---

## Database Relationship

```
User
 │
 ├── Post
 ├── Post
 └── Post
```

One User can have many Posts.

Each Post belongs to one User.

---

## Request

```
GET /users/1/posts
```

---

## Response

```json
[]
```

Since no posts were added to the database yet, the endpoint returns an empty list.

---

## What I Learned

- What a Foreign Key is.
- One-to-Many relationships.
- How relationship() works in SQLAlchemy.
- How tables are connected together.

---

# Important SQLAlchemy Concepts Learned

## Engine

Creates the connection between FastAPI and the database.

---

## SessionLocal

Creates a new database session for each request.

---

## Base

Base class inherited by all SQLAlchemy models.

---

## get_db()

Creates a database session using yield and automatically closes it after the request.

---

## CRUD Operations

### Create

```python
db.add()
db.commit()
db.refresh()
```

### Read

```python
db.query()
.filter()
.first()
.all()
```

### Delete

```python
db.delete()
db.commit()
```

---

## Schema vs Model

### SQLAlchemy Model

- Represents database tables.
- Used to communicate with the database.

Example:

- User
- Post

### Pydantic Schema

- Validates request data.
- Formats API responses.

Example:

- UserCreate
- UserRead

The API always returns Pydantic schemas instead of SQLAlchemy models.

---

# Alembic

The Day 3 topics also included Alembic for database migrations.

Topics covered:

- alembic init
- alembic revision --autogenerate
- alembic upgrade head

These commands are used to manage database schema changes in real-world projects instead of relying on Base.metadata.create_all().

---

# Summary

By completing this project, I learned how to:

- Connect FastAPI with SQLite using SQLAlchemy.
- Create SQLAlchemy models.
- Create Pydantic schemas.
- Perform Create, Read, and Delete operations.
- Use Dependency Injection with get_db().
- Implement pagination using skip and limit.
- Handle HTTP exceptions.
- Create one-to-many relationships using ForeignKey and relationship().
- Build REST APIs following FastAPI best practices.

This project provided hands-on experience with integrating a database into a FastAPI application and implementing CRUD operations using SQLAlchemy.