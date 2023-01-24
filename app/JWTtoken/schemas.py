from pydantic import BaseModel


class Tokenizer(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None