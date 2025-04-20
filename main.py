from fastapi import FastAPI
from routes import tasks, users,admin  # Ensure both routers are imported

app = FastAPI()

# Include the routes
app.include_router(tasks.router, prefix="/api/tasks")  # Make tasks accessible at /api/tasks
app.include_router(users.router, prefix="/api/users")  # Make users accessible at /api/users
app.include_router(admin.router, prefix="/api/admin")  # Make users accessible at /api/users

