from pydantic import BaseModel


class AddActor(BaseModel):
    name: str
    headshot: str
    id_imdb_actor: str

    class Config():
        orm_mode = True


class ViewActor(BaseModel):
    id: int
    name: str
    headshot: str
    id_imdb_actor: str

    class Config():
        orm_mode = True
