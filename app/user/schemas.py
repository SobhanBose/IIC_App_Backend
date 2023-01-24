from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    name: str = Field(...)
    email: EmailStr = Field(...)
    contact_no: int = Field(...)
    pic: str