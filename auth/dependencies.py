# FastAPI dependencies
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from schemas import UserInDB
from auth.auth import SECRET_KEY, ALGORITHM
import os
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "somehashedpassword123"
    }
}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        user_data = fake_users_db.get(username)
        if user_data is None:
           raise credentials_exception

        return UserInDB(**user_data)  # Return user data (you can expand this as needed)
    except JWTError:
        raise credentials_exception
