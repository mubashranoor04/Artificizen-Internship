from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test 1: Register User
def test_register():

    response = client.post(
        "/auth/register",
        json={
            "username": "mubashra",
            "email": "mubashra@gmail.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

# Test 2: Login
def test_login():

    response = client.post(
        "/auth/login",
        json={
            "username": "mubashra",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

# Test 3: Unauthorized Access
def test_unauthorized():

    response = client.get("/tasks/")

    assert response.status_code == 401

# Test 4: Create Task
def test_create_task():

    login = client.post(
        "/auth/login",
        json={
            "username": "mubashra",
            "password": "password123"
        }
    )
    token = login.json()["access_token"]

    response = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Learn FastAPI",
            "description": "Complete capstone",
            "status": "pending",
            "due_date": "2026-07-20"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Learn FastAPI"

# Test 5: Get Tasks
def test_get_tasks():

    login = client.post(
        "/auth/login",
        json={
            "username": "mubashra",
            "password": "password123"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)