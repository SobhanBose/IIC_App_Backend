from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    name: str
    email: str
    contact_no: int
    pic: str