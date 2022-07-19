from typing import List
from fastapi import APIRouter, Depends

from ..schemas.directors_in_movie import AddDirectorsInMovie, ViewDirectorsInMovie
from ..models import DirectorInMovie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/directors-in-movie',
    tags=['Diretores do filme']
)


@router.post('/')
def adicionar_diretores_no_filme(request: AddDirectorsInMovie, db: Session = Depends(get_db)):
    novo_diretor = DirectorInMovie(**request.dict())
    db.add(novo_diretor)
    db.commit()
    db.refresh(novo_diretor)

    return novo_diretor


@router.get('/{movie_id}', response_model=List[ViewDirectorsInMovie])
def retornar_filme_com_diretores(movie_id: int, db: Session = Depends(get_db)):
    diretores_do_filme = db.query(DirectorInMovie).filter(
        DirectorInMovie.movie_id == movie_id).all()
    return diretores_do_filme


@router.delete('/{director_in_movie_id}')
def deletar_diretor_do_filme(director_in_movie_id: int, db: Session = Depends(get_db)):
    db.query(DirectorInMovie).filter(DirectorInMovie.id == director_in_movie_id).delete(
        synchronize_session=False)
    db.commit()

    return "Diretor deletado com sucesso!"
