from typing import List
from fastapi import APIRouter, Depends

from ..schemas.actors_in_movie import AddActorsInMovie, ViewActorsInMovie
from ..models import ActorInMovie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/actors-in-movie',
    tags=['Atores do filme']
)


@router.post('/')
def adicionar_atores_no_filme(request: AddActorsInMovie, db: Session = Depends(get_db)):
    novo_ator = ActorInMovie(**request.dict())
    db.add(novo_ator)
    db.commit()
    db.refresh(novo_ator)

    return novo_ator


@router.get('/{movie_id}', response_model=List[ViewActorsInMovie])
def retornar_filme_com_atores(movie_id: int, db: Session = Depends(get_db)):
    atores_do_filme = db.query(ActorInMovie).filter(
        ActorInMovie.movie_id == movie_id).all()
    return atores_do_filme


@router.delete('/{actor_in_movie_id}')
def deletar_ator_do_filme(actor_in_movie_id: int, db: Session = Depends(get_db)):
    db.query(ActorInMovie).filter(ActorInMovie.id == actor_in_movie_id).delete(
        synchronize_session=False)
    db.commit()

    return "Ator deletado com sucesso!"
