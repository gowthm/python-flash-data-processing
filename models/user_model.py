from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserModel(BaseModel):
    name: str =Field(..., min_length=2, max_length=10)
    email: EmailStr
    age: int | None = Field(default=None)

class UserUpdateModel(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
