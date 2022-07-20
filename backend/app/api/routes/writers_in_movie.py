from typing import List
from fastapi import APIRouter, Depends

from ..schemas.writers_in_movie import AddWritersInMovie, ViewWritersInMovie
from ..models import WriterInMovie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/writers-in-movie',
    tags=['Escritores do filme']
)


@router.post('/')
def adicionar_escritores_no_filme(request: AddWritersInMovie, db: Session = Depends(get_db)):
    novo_escritor = WriterInMovie(**request.dict())
    db.add(novo_escritor)
    db.commit()
    db.refresh(novo_escritor)

    return novo_escritor


@router.get('/{movie_id}', response_model=List[ViewWritersInMovie])
def retornar_filme_com_escritores(movie_id: int, db: Session = Depends(get_db)):
    escritores_do_filme = db.query(WriterInMovie).filter(
        WriterInMovie.movie_id == movie_id).all()
    return escritores_do_filme


@router.delete('/{writer_in_movie_id}')
def deletar_escritor_do_filme(writer_in_movie_id: int, db: Session = Depends(get_db)):
    db.query(WriterInMovie).filter(WriterInMovie.id == writer_in_movie_id).delete(
        synchronize_session=False)
    db.commit()

    return "Escritor deletado com sucesso!"
