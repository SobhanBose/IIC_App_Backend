from pydantic import BaseModel, Field

class Team(BaseModel):
    username: str = Field(...)