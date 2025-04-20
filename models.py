from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

# Request model - used for POST and PUT
class TaskCreate(BaseModel):
    title: str
    description: str

# Response model - what the client gets
class Task(TaskCreate):
    id: UUID
    completed: bool = False

# Optional: model that includes MongoDB’s native _id (not returned to client)
class MongoTask(Task):
    mongo_id: Optional[str] = Field(alias="_id")  # ✅ alias keeps MongoDB compatibility
