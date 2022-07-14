from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class VerifyToken(BaseModel):
    email: str
    token_to_verify: str
    hashed_token: str
