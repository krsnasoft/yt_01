from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    # name: Optional[str] = None
    name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    # password: Optional[str] = None
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True