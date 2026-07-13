from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test1
def test_create_user():

    response = client.post(
        "/users/",
        json={
            "name": "Mubashra",
            "email": "mubashranoor04@gmail.com"
        }
    )
    assert response.status_code == 201

    assert response.json()["message"] == "User created successfully"

    assert response.json()["user"]["name"] == "Mubashra"

    assert response.json()["user"]["email"] == "mubashranoor04@gmail.com"

#test2
def test_duplicate_email():

    # First user
    client.post(
        "/users/",
        json={
            "name": "Mubashra",
            "email": "mubashranoor04@gmail.com"
        }
    )
    # Duplicate email
    response = client.post(
        "/users/",
        json={
            "name": "Noor",
            "email": "mubashranoor04@gmail.com"
        }
    )
    assert response.status_code == 409

    assert response.json()["detail"] == "Email already exists"
#test 3 
def test_protected_route():
    response = client.get("/auth/me")
    assert response.status_code == 401
#test4
def test_login():

    response = client.post("/auth/login")

    assert response.status_code == 200

    assert response.json()["access_token"] == "fake-jwt-token"

#test5
def test_get_users():

    response = client.get("/users/")

    assert response.status_code == 200