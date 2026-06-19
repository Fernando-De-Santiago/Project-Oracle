from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserRegister(BaseModel):
    email : EmailStr
    username : str = Field(min_length=10, max_length=20)
    password: str = Field(min_length=12)

class UserLogin(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: int
    username : str
    email: EmailStr
    created_at: datetime
    model_config = {"from_attributes": True}