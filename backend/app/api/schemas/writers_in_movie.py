from pydantic import BaseModel

from ..schemas.writers import ViewWriter


class AddWritersInMovie(BaseModel):
    movie_id: int
    writer_id: int

    class Config():
        orm_mode = True


class ViewWritersInMovie(BaseModel):
    writer: ViewWriter

    class Config():
        orm_mode = True
