from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings, Field


# class Settings(BaseSettings):
#     DB_URL: str = Field(..., env='DATABASE_URL')


# settings = Settings()

# engine = create_engine(
#     settings.DB_URL
# )


HOST = 'localhost'
USERNAME = 'postgres'
PASSWORD = '75369875'
PORT = '5432'
DATABASE_NAME = 'choose'

CONNECTION = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE_NAME}'


engine = create_engine(
    CONNECTION
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()