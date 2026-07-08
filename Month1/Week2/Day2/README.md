# FastAPI Training – Day 2

## Overview

This day focuses on **Pydantic Models and Request/Response Validation** in FastAPI. The exercises demonstrate how FastAPI uses Pydantic to validate incoming data, serialize responses, enforce business rules, and generate API documentation automatically.

## Project Structure

```text
Day2/
│
├── user_create.py
├── field_constraint.py
├── response_model.py
├── nested_models.py
├── field_validator.py
├── item_schemas.py
├── requirements.txt
└── README.md
```

---

## Topics Covered

### 1. BaseModel

`BaseModel` is the foundation of data validation in FastAPI.

Instead of using regular Python classes, FastAPI relies on Pydantic models to:

- Validate incoming data
- Convert JSON into Python objects
- Generate API documentation
- Produce descriptive validation errors

Example:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
```

---

### 2. Request Body

When a function parameter is annotated with a Pydantic model, FastAPI automatically expects the data to be sent in the request body.

Example:

```python
@app.post("/users")
def create_user(user: UserCreate):
    return user
```

Request:

```json
{
    "name": "Ali",
    "email": "ali@example.com",
    "age": 22
}
```

---

### 3. Field Validation

`Field()` provides additional validation rules beyond Python data types.

Example:

```python
from pydantic import Field

age: int = Field(ge=18, le=120)
```

Constraints used:

| Constraint | Description |
|------------|-------------|
| `ge` | Greater than or equal to |
| `gt` | Greater than |
| `le` | Less than or equal to |
| `lt` | Less than |
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |
| `pattern` | Regular expression validation |

If validation fails, FastAPI automatically returns a **422 Unprocessable Entity** response.

---

### 4. Email Validation

Two approaches were explored.

Using a regular expression:

```python
email: str = Field(
    pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
)
```

Recommended approach:

```python
from pydantic import EmailStr

email: EmailStr
```

`EmailStr` requires the `email-validator` package.

---

### 5. Request and Response Models

The data received from the client is often different from the data returned by the server.

Request schema:

```python
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
```

Response schema:

```python
class UserRead(BaseModel):
    id: int
    name: str
    email: str
```

Sensitive fields such as passwords should never be included in API responses.

---

### 6. Response Models

FastAPI allows response validation through the `response_model` parameter.

Example:

```python
@app.post("/users", response_model=UserRead)
```

Benefits:

- Validates outgoing responses
- Removes fields not included in the schema
- Generates accurate API documentation
- Prevents accidental exposure of sensitive information

---

### 7. Nested Models

Nested models represent complex JSON objects.

Example request:

```json
{
    "name": "Ali",
    "email": "ali@example.com",
    "age": 22,
    "address": {
        "city": "Lahore",
        "country": "Pakistan"
    }
}
```

Models:

```python
class Address(BaseModel):
    city: str
    country: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    address: Address
```

Advantages:

- Reusable schemas
- Cleaner code
- Better organization
- Easier maintenance

---

### 8. Custom Validation with field_validator

Business rules that cannot be expressed using `Field()` can be implemented using `@field_validator`.

Example:

```python
from pydantic import field_validator

class UserCreate(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        for char in value:
            if char.isdigit():
                raise ValueError("Name cannot contain numbers.")
        return value
```

The validator executes before the route function.

If validation fails:

- The route function is not executed.
- FastAPI returns a 422 response.

---

### 9. Separate Create and Read Schemas

Request schema:

```python
class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool
```

Response schema:

```python
class ItemRead(BaseModel):
    name: str
    price: float
    in_stock: bool
    created_at: str
```

The client provides only the data required to create the resource.

The server generates additional fields such as:

- `id`
- `created_at`
- `updated_at`

---

## Files Implemented

| File | Description |
|------|-------------|
| `user_create.py` | Request body using `BaseModel` |
| `response_model.py` | Request and response schemas |
| `nested_models.py` | Nested Pydantic models |
| `field_validator.py` | Custom validation |
| `item_schemas.py` | Separate Create and Read schemas |

---

## Validation Flow

```text
Client Request
      │
      ▼
FastAPI
      │
      ▼
Pydantic Model
      │
      ▼
Field Validation
      │
      ▼
Custom Validators
      │
      ▼
Route Function
      │
      ▼
Response Model Validation
      │
      ▼
Client Response
```

---

## Common Validation Errors

### Missing Required Field

```json
{
    "name": "Ali"
}
```

Result:

```
422 Unprocessable Entity
```

---

### Invalid Data Type

```json
{
    "age": "twenty"
}
```

Result:

```
422 Unprocessable Entity
```

---

### Constraint Violation

```json
{
    "age": 15
}
```

Result:

```
422 Unprocessable Entity
```

---

### Custom Validation Failure

```json
{
    "name": "Ali123"
}
```

Result:

```
422 Unprocessable Entity
```

---

## Key Takeaways

- `BaseModel` enables automatic validation and serialization.
- Pydantic models used as function parameters are interpreted as request bodies.
- `Field()` adds constraints beyond Python data types.
- `EmailStr` is preferred over manual regular expressions.
- Separate request and response schemas improve security and maintainability.
- `response_model` validates and filters outgoing responses.
- Nested models simplify complex JSON structures.
- `@field_validator` allows custom business rule validation.
- FastAPI automatically generates interactive API documentation based on Pydantic models.

---

## Dependencies

```text
fastapi
uvicorn[standard]
pydantic
email-validator
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Conclusion

Day 2 introduced the core concepts required to build reliable and well-structured FastAPI applications. Pydantic models provide automatic validation, request parsing, response serialization, and API documentation while reducing boilerplate code. Separating request and response schemas, using nested models, and implementing custom validators are fundamental practices that improve code quality, maintainability, and security in real-world FastAPI projects.