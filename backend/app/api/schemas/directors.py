from pydantic import BaseModel


class AddDirector(BaseModel):
    name: str

    class Config():
        orm_mode = True


class ViewDirector(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
