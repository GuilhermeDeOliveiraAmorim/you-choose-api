from pydantic import BaseModel

from ..schemas.actors import ViewActor


class AddActorsInMovie(BaseModel):
    movie_id: int
    actor_id: int

    class Config():
        orm_mode = True


class ViewActorsInMovie(BaseModel):
    actor: ViewActor

    class Config():
        orm_mode = True
