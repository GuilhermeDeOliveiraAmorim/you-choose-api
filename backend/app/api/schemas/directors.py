from pydantic import BaseModel


class AddDirector(BaseModel):
    name: str
    headshot: str
    id_imdb_director: str

    class Config():
        orm_mode = True


class ViewDirector(BaseModel):
    id: int
    name: str
    headshot: str
    id_imdb_director: str

    class Config():
        orm_mode = True
