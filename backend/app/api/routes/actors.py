from typing import List
from fastapi import APIRouter, Depends

from ..schemas.actors import AddActor, ViewActor
from ..models import Actor
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/actors',
    tags=['Atores']
)


@router.get('/', response_model=List[ViewActor])
def retornar_lista_de_atores(db: Session = Depends(get_db)):
    lista_atores = db.query(Actor).all()
    return lista_atores


@router.post('/')
def cadastrar_um_novo_ator(request: AddActor, db: Session = Depends(get_db)):
    novo_ator = Actor(**request.dict())
    db.add(novo_ator)
    db.commit()
    db.refresh(novo_ator)

    return novo_ator


@router.get('/{actor_id}')
def retornar_ator(actor_id: int, db: Session = Depends(get_db)):
    actor = db.query(Actor).get(actor_id)
    return actor


@router.delete('/{actor_id}')
def deletar_ator(actor_id: int, db: Session = Depends(get_db)):
    db.query(Actor).filter(Actor.id == actor_id).delete(
        synchronize_session=False)
    db.commit()

    return "Ator deletado com sucesso!"


@router.put('/{actor_id}')
def atualizar_informacoes_do_ator(request: AddActor, actor_id: int, db: Session = Depends(get_db)):

    db.query(Actor).filter(Actor.id == actor_id).update(request.dict())
    db.commit()

    return "Ator atualizado com sucesso!"
