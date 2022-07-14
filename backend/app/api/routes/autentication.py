from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, token
from sqlalchemy.orm import Session
from ..utils.hashing import Hash
import secrets
import string
from typing import List


router = APIRouter(prefix='/api/login',
                   tags=['Autenticação'])


@router.post('')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'O usuário {request.username} não existe')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Suas credenciais estão erradas')
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
