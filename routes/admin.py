from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
from schemas import UserInDB

router = APIRouter()

@router.get("/dash")
def read_admin_data(current_user: UserInDB = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}. Welcome to the admin panel!"}