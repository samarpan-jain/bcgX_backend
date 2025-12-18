from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    email: EmailStr = Field(description="The email of the user", example="user@example.com", max_length=150)
    name: str = Field(description="The name of the user", example="John Doe", max_length=150)
    role: str = Field(description="The role of the user", example="admin", max_length=50)
    password: str = Field(description="The password of the user", example="password123", max_length=150, min_length=8)

class UserRes(BaseModel):
    id: str
    email: EmailStr
    name: str
    role: str

class UserDTO(UserBase):
    class Config:
        from_attributes = True