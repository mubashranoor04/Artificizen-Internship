from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db, get_current_user
from models import Task, User
from schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()

# CREATE TASK
@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# GET ALL TASKS
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    query = db.query(Task).filter(
        Task.owner_id == current_user.id
    )

    if status:
        query = query.filter(Task.status == status)

    return query.all()

# GET ONE TASK
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task

# UPDATE TASK
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if updated_task.title is not None:
        task.title = updated_task.title

    if updated_task.description is not None:
        task.description = updated_task.description

    if updated_task.status is not None:
        task.status = updated_task.status

    if updated_task.due_date is not None:
        task.due_date = updated_task.due_date

    db.commit()
    db.refresh(task)

    return task

# DELETE TASK
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }