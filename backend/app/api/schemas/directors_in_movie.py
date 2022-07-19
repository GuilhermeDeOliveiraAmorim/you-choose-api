from pydantic import BaseModel

from ..schemas.directors import ViewDirector


class AddDirectorsInMovie(BaseModel):
    movie_id: int
    genre_id: int

    class Config():
        orm_mode = True


class ViewDirectorsInMovie(BaseModel):
    genre: ViewDirector

    class Config():
        orm_mode = True
