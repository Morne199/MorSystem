from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from auth.dependencies import get_current_user  # Import the dependency to check for a valid user
from models import TaskCreate, Task
from db import task_collection
from uuid import uuid4, UUID
from typing import List
from jobs.background_tasks import send_email_notification

router = APIRouter()

def task_serializer(task) -> Task:
    return Task(
        id=UUID(task["id"]),
        title=task["title"],
        description=task["description"],
        completed=task["completed"]
    )

# Protecting the /tasks route with the JWT dependency
@router.get("/tasks", response_model=List[Task])
async def get_tasks(user: dict = Depends(get_current_user)):  # Added user dependency
    tasks = await task_collection.find().to_list(100)
    return [task_serializer(t) for t in tasks]

# Protecting the create_task route with the JWT dependency
@router.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate, background_tasks: BackgroundTasks, user: dict = Depends(get_current_user)):  # Added user dependency
    new_task = {
        "id": str(uuid4()),
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    await task_collection.insert_one(new_task)

    # Run background task
    background_tasks.add_task(send_email_notification, task.title)

    return task_serializer(new_task)

@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: UUID, user: dict = Depends(get_current_user)):  # Added user dependency
    task = await task_collection.find_one({"id": str(task_id)})
    if task:
        return task_serializer(task)
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, updated: TaskCreate, user: dict = Depends(get_current_user)):  # Added user dependency
    update_data = {
        "title": updated.title,
        "description": updated.description
    }
    result = await task_collection.update_one({"id": str(task_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = await task_collection.find_one({"id": str(task_id)})
    return task_serializer(updated_task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: UUID, user: dict = Depends(get_current_user)):  # Added user dependency
    result = await task_collection.delete_one({"id": str(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
