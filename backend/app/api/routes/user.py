from fastapi import APIRouter, Depends
from ..utils.hashing import Hash
from ..schemas.user import AddUser
from ..models import User
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/users',
    tags=['Usuário']
)


@router.post('/')
def cadastrar_usuario(request: AddUser, db: Session = Depends(get_db)):
    novo_usuario = User(email=request.email,
                        password=Hash.bcrypt(request.password))
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
