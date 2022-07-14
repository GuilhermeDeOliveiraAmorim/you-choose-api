from typing import List
from fastapi import APIRouter, Depends

from ..schemas.genres_in_movie import AddGenresInMovie, ViewGenresInMovie
from ..schemas.movies import AddMovie, ViewMovie
from ..models import GenreInMovie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/genres-in-movie',
    tags=['Gêneros do filme']
)


@router.post('/')
def adicionar_generos_no_filme(request: AddGenresInMovie, db: Session = Depends(get_db)):
    novo_genero = GenreInMovie(**request.dict())
    db.add(novo_genero)
    db.commit()
    db.refresh(novo_genero)

    return novo_genero


@router.get('/{movie_id}', response_model=List[ViewGenresInMovie])
def retornar_filme_com_generos(movie_id: int, db: Session = Depends(get_db)):
    generos_do_filme = db.query(GenreInMovie).filter(
        GenreInMovie.movie_id == movie_id).all()
    return generos_do_filme


@router.delete('/{genre_in_movie_id}')
def deletar_genero_do_filme(genre_in_movie_id: int, db: Session = Depends(get_db)):
    db.query(GenreInMovie).filter(GenreInMovie.id == genre_in_movie_id).delete(
        synchronize_session=False)
    db.commit()

    return "Gênero deletado com sucesso!"
