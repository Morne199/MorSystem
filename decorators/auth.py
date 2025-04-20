from fastapi import HTTPException

def authenticate(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if user != "admin":
            raise HTTPException(status_code=403, detail="Access denied")
        return func(*args, **kwargs)
    return wrapper
