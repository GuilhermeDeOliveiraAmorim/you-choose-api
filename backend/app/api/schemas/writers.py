from pydantic import BaseModel


class AddWriter(BaseModel):
    name: str
    headshot: str
    id_imdb_writer: str

    class Config():
        orm_mode = True


class ViewWriter(BaseModel):
    id: int
    name: str
    headshot: str
    id_imdb_writer: str

    class Config():
        orm_mode = True
