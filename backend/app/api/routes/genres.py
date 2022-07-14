from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from ..schemas.genres import AddGenre, ViewGenre
from ..models import Genre, Movie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/genres',
    tags=['Gêneros']
)


@router.get('/', response_model=List[ViewGenre])
def retornar_lista_de_generos(db: Session = Depends(get_db)):
    lista_generos = db.query(Genre).all()
    return lista_generos


@router.post('/')
def cadastrar_um_novo_genero(request: AddGenre, db: Session = Depends(get_db)):
    novo_genero = Genre(**request.dict())
    db.add(novo_genero)
    db.commit()
    db.refresh(novo_genero)

    return novo_genero


@router.get('/{genre_id}')
def retornar_genero(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).get(genre_id)
    return genre


@router.delete('/{genre_id}')
def deletar_genero(genre_id: int, db: Session = Depends(get_db)):
    db.query(Genre).filter(Genre.id == genre_id).delete(
        synchronize_session=False)
    db.commit()

    return "Gênero deletado com sucesso!"


@router.put('/{genre_id}')
def atualizar_informacoes_do_genero(request: AddGenre, genre_id: int, db: Session = Depends(get_db)):

    db.query(Genre).filter(Genre.id == genre_id).update(request.dict())
    db.commit()

    return "Gênero atualizado com sucesso!"
