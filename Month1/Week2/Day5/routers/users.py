from fastapi import APIRouter, BackgroundTasks, HTTPException, status

router = APIRouter()

# Fake database (for practice only)
users_db = []

# Background Task
def send_welcome_email(email: str):
    print("=" * 40)
    print(f"Welcome email sent to {email}")
    print("=" * 40)

# Get all users
@router.get("/")
def get_users():
    return users_db

# Get one user
@router.get("/{user_id}")
def get_user(user_id: int):

    if user_id >= len(users_db):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users_db[user_id]

# Create user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(
    user: dict,
    background_tasks: BackgroundTasks
):
# Check duplicate email
    for existing_user in users_db:
        if existing_user["email"] == user["email"]:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

    users_db.append(user)

# Background Task
    background_tasks.add_task(
        send_welcome_email,
        user["email"]
    )

    return {
        "message": "User created successfully",
        "user": user
    }
# Delete user
@router.delete("/{user_id}")
def delete_user(user_id: int):

    if user_id >= len(users_db):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users_db.pop(user_id)

    return {
        "message": "User deleted"
    }