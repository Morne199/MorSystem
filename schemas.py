from pydantic import BaseModel

# schemas.py
class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

