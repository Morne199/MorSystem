import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

MONGODB_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]

# This is your tasks collection
task_collection = db.get_collection("tasks")
