from .tasks import router as tasks_router
from .users import router as users_router
from .admin import router as admin_router


__all__ = ["tasks_router","users_router","admin_router"]