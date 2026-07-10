Day 4 - Authentication & Security (FastAPI)
Overview
This project demonstrates how to implement secure user authentication, authorization, and data encryption in a FastAPI application. During this practice, I learned how to securely hash passwords using Passlib, create and verify JSON Web Tokens (JWT) for stateless user sessions, use FastAPI's built-in OAuth2 password flows, protect private API endpoints with dependency injection, and apply Role-Based Access Control (RBAC) to enforce security layers.

Technologies Used
Python

FastAPI

SQLAlchemy

SQLite

Pydantic

Passlib (with Bcrypt)

Python-Jose (for JWTs)

Python-Multipart

Project Structure
Plaintext
fastapi_sqlalchemy_day3/Day4/
│
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── main.py
├── users.db
├── .env
├── requirements.txt
└── README.md
Files Description
database.py
Responsible for setting up the SQLite engine, database session factory (SessionLocal), declarative Base metadata model, and providing the localized cleanup pipeline.

models.py
Contains SQLAlchemy ORM definitions for tables mapping data directly onto SQLite records. Features a newly added tracking string field for access permissions.

schemas.py
Houses Pydantic v2 data models parsing strict input structure definitions, response formatting logic, and automatic database attribute extraction conversions.

auth.py
Handles the core security layers including password hashing configurations, JWT encryption generation pipelines, token expiration routines, and authentication route guards.

main.py
Contains the central FastAPI app routing configurations, application startups, dependency injections, dynamic operational definitions, and CRUD path endpoints.

Practice Question 1
Question
Write a hash_password() and verify_password() utility using passlib. Test them in isolation before wiring into routes.

Files Used
auth.py

What was implemented
Instantiated a CryptContext object leveraging the secure bcrypt engine.

Configured robust abstractions parsing plain strings safely into irreversible mathematical hashes.

Implemented corresponding conditional structures validating plain passwords matching database records securely.

What I Learned
Never store plaintext passwords under any circumstances.

How the bcrypt algorithm works to generate secure, salted hashes.

The separation of cryptographic configurations inside isolated security modules.

Practice Question 2
Question
Create a POST /auth/register route that accepts username + password, hashes the password, and saves the user.

Files Used
schemas.py

main.py

What was implemented
Drafted dedicated validation blocks parsing registration schemas cleanly.

Set up unique record lookups protecting database integrity against duplicate usernames.

Implemented the register path securely, generating dynamic salted hashes before committing records.

Request
JSON
POST /auth/register
{
    "username": "mubashra",
    "password": "supersecurepassword123"
}
Response
JSON
{
    "id": 1,
    "username": "mubashra",
    "role": "user"
}
What I Learned
Intercepting request schemas to process underlying fields recursively.

Verifying unique application state parameters prior to execution pipelines.

Practice Question 3
Question
Create a POST /auth/token route using OAuth2PasswordRequestForm that verifies credentials and returns a signed JWT.

Files Used
auth.py

main.py

What was implemented
Replaced JSON body schemas with standard OAuth2PasswordRequestForm parsing form-data structures.

Validated credentials securely by calling isolated password verifiers against query states.

Generated signed tokens containing custom dictionary data payloads.

Request
Plaintext
POST /auth/token
Body (form-data):
username: mubashra
password: supersecurepassword123
Response
JSON
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
What I Learned
Why standard form-data elements are globally uniform requirements for standard browser credential pipelines.

Installing python-multipart to parse form uploads inside modern asynchronous structures.

Attaching dictionary scopes (sub, role) within structural cryptograms.

Practice Question 4
Question
Write a get_current_user dependency that reads the Authorization: Bearer <token> header, decodes the JWT, and returns the user or raises 401.

Files Used
auth.py

What was implemented
Leveraged OAuth2PasswordBearer variables parsing bearer strings uniformly from request metadata.

Constructed safe payload execution blocks using jwt.decode configurations.

Created custom exceptions validating claims and raising strict HTTP status warnings on malformed inputs.

What I Learned
Decoding encoded structures using matching algorithm strings.

Validating standard token signatures dynamically on every backend transaction safely.

Practice Question 5
Question
Protect GET /users/me with the get_current_user dependency so only authenticated users can access it.

Files Used
main.py

What was implemented
Attached the get_current_user functional dependants onto targeted profiles routes.

Returned the user record returned by the verification pipeline.

Request
Plaintext
GET /users/me
Headers: Authorization: Bearer <token>
Response
JSON
{
    "id": 1,
    "username": "mubashra",
    "role": "user"
}
Invalid Request (No/Expired Token)
JSON
Status Code: 401 Unauthorized
{
    "detail": "Invalid token"
}
What I Learned
Restricting open pathways from anonymous exposure using dependency injections.

Intercepting dynamic request parameters directly through functional wrapper constraints.

Practice Question 6
Question
Add a role field to your user model. Write a require_admin dependency that raises 403 if the current user is not an admin, and apply it to a DELETE /users/{id} route.

Files Used
models.py

auth.py

main.py

What was implemented
Extended user database tables with an explicit access role tracking column tracking authorization levels.

Formulated chained dependency flows validating parameters passed downwards into administrative functions.

Attached custom error layers raising forbidden responses to unprivileged requests.

Request (Authenticated Admin)
Plaintext
DELETE /users/2
Headers: Authorization: Bearer <admin_token>
Response
Plaintext
204 No Content
Invalid Request (Standard User Account)
JSON
Status Code: 403 Forbidden
{
    "detail": "You do not have permission to perform this action"
}
What I Learned
The critical architectural differences between Authentication (Who you are) and Authorization (What you can do).

Nesting functional dependency trees cleanly within FastAPI.

Important Security Concepts Learned
Password Hashing
Storing raw access strings inside any accessible state compromises database integrity entirely. Standard algorithms apply secure calculations making recovery impossible.

Stateless JWT Frameworks
Instead of recording long-lived active login state metrics on host engines across varying systems, backends can issue tamper-proof cryptograms validating authentication claims autonomously.

Token Expiration
Using explicit .env configurations to append timestamped limits (exp) onto payload structures protects state changes from token-sniffing exploits.

Summary
By completing this practice day, I successfully learned how to structure authentication middleware components securely, isolate secret global configurations inside explicit environments, generate validated tokens, inspect dynamic scopes inside endpoints, and implement robust role-based access control (RBAC).
