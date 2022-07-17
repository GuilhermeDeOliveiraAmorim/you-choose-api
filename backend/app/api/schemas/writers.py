from pydantic import BaseModel


class AddWriter(BaseModel):
    name: str

    class Config():
        orm_mode = True


class ViewWriter(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
