from pydantic import BaseModel

from ..schemas.genres import ViewGenre


class AddGenresInMovie(BaseModel):
    movie_id: int
    genre_id: int

    class Config():
        orm_mode = True


class ViewGenresInMovie(BaseModel):
    genre: ViewGenre

    class Config():
        orm_mode = True
