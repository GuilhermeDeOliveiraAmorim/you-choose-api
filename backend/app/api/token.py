from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from . import database, models
from sqlalchemy.orm import Session


SECRET_KEY = "e14b9285c1d7c676fa929f3a832c678f06efcf02a72d8a1f76377b127b14adac"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception, db: Session = Depends(database.get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
