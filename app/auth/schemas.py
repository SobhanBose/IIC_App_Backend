from pydantic import BaseModel, Field

class Login(BaseModel):
    username: str = Field(...)
    password: str = Field(...)