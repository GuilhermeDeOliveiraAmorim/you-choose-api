from datetime import date
from pydantic import BaseModel


class AddMovie(BaseModel):
    title: str
    year: int
    imdbRating: float
    youchooseRating: float
    poster: str

    class Config():
        orm_mode = True


class ViewMovie(BaseModel):
    id: int
    title: str

    class Config():
        orm_mode = True
