from typing import List
from fastapi import APIRouter, Depends

from ..schemas.writers import AddWriter, ViewWriter
from ..models import Writer
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/writers',
    tags=['Escritores']
)


@router.get('/', response_model=List[ViewWriter])
def retornar_lista_de_escritores(db: Session = Depends(get_db)):
    lista_escritores = db.query(Writer).all()
    return lista_escritores


@router.post('/')
def cadastrar_um_novo_escritor(request: AddWriter, db: Session = Depends(get_db)):
    novo_escritor = Writer(**request.dict())
    db.add(novo_escritor)
    db.commit()
    db.refresh(novo_escritor)

    return novo_escritor


@router.get('/{writer_id}')
def retornar_escritor(writer_id: int, db: Session = Depends(get_db)):
    writer = db.query(Writer).get(writer_id)
    return writer


@router.delete('/{writer_id}')
def deletar_escritor(writer_id: int, db: Session = Depends(get_db)):
    db.query(Writer).filter(Writer.id == writer_id).delete(
        synchronize_session=False)
    db.commit()

    return "Escritor deletado com sucesso!"


@router.put('/{writer_id}')
def atualizar_informacoes_do_escritor(request: AddWriter, writer_id: int, db: Session = Depends(get_db)):

    db.query(Writer).filter(Writer.id ==
                            writer_id).update(request.dict())
    db.commit()

    return "Escritor atualizado com sucesso!"
