from typing import List
from fastapi import APIRouter, Depends

from ..schemas.directors import AddDirector, ViewDirector
from ..models import Director, Movie
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/directors',
    tags=['Diretores']
)


@router.get('/', response_model=List[ViewDirector])
def retornar_lista_de_diretores(db: Session = Depends(get_db)):
    lista_diretores = db.query(Director).all()
    return lista_diretores


@router.post('/')
def cadastrar_um_novo_diretor(request: AddDirector, db: Session = Depends(get_db)):
    novo_diretor = Director(**request.dict())
    db.add(novo_diretor)
    db.commit()
    db.refresh(novo_diretor)

    return novo_diretor


@router.get('/{director_id}')
def retornar_diretor(director_id: int, db: Session = Depends(get_db)):
    director = db.query(Director).get(director_id)
    return director


@router.delete('/{director_id}')
def deletar_diretor(director_id: int, db: Session = Depends(get_db)):
    db.query(Director).filter(Director.id == director_id).delete(
        synchronize_session=False)
    db.commit()

    return "Diretor deletado com sucesso!"


@router.put('/{director_id}')
def atualizar_informacoes_do_diretor(request: AddDirector, director_id: int, db: Session = Depends(get_db)):

    db.query(Director).filter(Director.id ==
                              director_id).update(request.dict())
    db.commit()

    return "Diretor atualizado com sucesso!"
