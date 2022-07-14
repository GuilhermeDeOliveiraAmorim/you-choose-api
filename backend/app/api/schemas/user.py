from datetime import date
from pydantic import BaseModel


class AddUser(BaseModel):
    email: str
    password: str

    class Config():
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    password: str

    class Config():
        orm_mode = True
