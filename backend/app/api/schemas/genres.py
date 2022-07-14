from pydantic import BaseModel


class AddGenre(BaseModel):
    name: str

    class Config():
        orm_mode = True


class ViewGenre(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
