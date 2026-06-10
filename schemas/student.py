from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(min_length=10, max_length=10)
    department: str