from datetime import datetime, date
from http.client import HTTPException
from tracemalloc import stop
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from imdb import Cinemagoer
from sqlalchemy import null
from ..schemas.movies import AddMovie, ViewMovie
from ..models import Director, GenreInMovie, Movie, Genre, Writer
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas.user import User
from ..oath2 import get_current_user

router = APIRouter(
    prefix='/api/movies',
    tags=['Filmes']
)


@router.get('/')
def retornar_lista_de_filmes(db: Session = Depends(get_db)):

    lista_filmes = db.query(Movie).all()
    return lista_filmes


@router.post('/')
def cadastrar_um_novo_filme(request: AddMovie, db: Session = Depends(get_db)):
    novo_filme = Movie(**request.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)

    return novo_filme


@router.post('/{imdb_id}')
def cadastrar_um_novo_filme_com_imdb(imdb_id: str, request: AddMovie, db: Session = Depends(get_db)):

    movie = db.query(Movie).filter(Movie.imdb_id == imdb_id).first()

    if movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"O filme {movie.title} já existe no seu banco.")

    ia = Cinemagoer()

    imdb_movie = ia.get_movie(imdb_id)

    novo_filme = Movie(
        imdb_id=imdb_id,
        title=imdb_movie['title'],
        year=imdb_movie['year'],
        imdbRating=imdb_movie['rating'],
        poster=imdb_movie['full-size cover url'],
        youchooseRating=0
    )

    db.add(novo_filme)
    db.commit()

    lista_generos = db.query(Genre.name).all()
    lista_diretores = db.query(Director.name).all()
    idMovie = db.query(Movie.id).filter(Movie.imdb_id == imdb_id).first()

    lista_generos = [x[0] for x in lista_generos]
    lista_diretores = [x[0] for x in lista_diretores]

    for x in imdb_movie['genres']:

        genreName = x

        if genreName not in lista_generos:

            db.add(Genre(name=genreName))
            db.commit()
            idGenre = db.query(Genre.id).filter(
                Genre.name == genreName).first()

            print(f"O gênero {genreName} foi cadastrado!")

            db.add(GenreInMovie(movie_id=idMovie, genre_id=idGenre))
            db.commit()

            print(
                f"A relação gênero {idGenre} com filme {idMovie} foi cadastrada!")

        else:

            print(f"O gênero {genreName} já está cadastrado!")

            idGenre = db.query(Genre.id).filter(
                Genre.name == genreName).first()

            db.add(GenreInMovie(movie_id=idMovie, genre_id=idGenre))
            db.commit()

            print(
                f"A relação gênero {idGenre} com filme {idMovie} foi cadastrada!")

    for x in imdb_movie['directors']:
        directorName = x['name']
        if directorName not in lista_diretores:
            db.add(Director(name=directorName))
            print(f"O diretor {directorName} foi cadastrado!")
        else:
            print(f"O diretor {directorName} já está cadastrado!")

    for writer in imdb_movie['writers']:
        if writer.personID is not None:
            person = ia.get_person(writer.personID)
            writerName = person['name']
            lista_escritores = db.query(Writer.name).all()
            lista_escritores = [x[0] for x in lista_escritores]
            if writerName not in lista_escritores:
                db.add(Writer(name=writerName))
                db.commit()
                print(f"O escritor {writerName} foi cadastrado!")
            else:
                print(f"O escritor {writerName} já está cadastrado!")

    db.refresh(novo_filme)

    return novo_filme


@router.get('/{filme_id}')
def retornar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(Movie).get(filme_id)
    return filme


@router.delete('/{filme_id}')
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    db.query(Movie).filter(Movie.id == filme_id).delete(
        synchronize_session=False)
    db.commit()

    return "Filme deletado com sucesso!"


@router.put('/{filme_id}')
def atualizar_informacoes_do_filme(request: AddMovie, filme_id: int, db: Session = Depends(get_db)):

    db.query(Movie).filter(Movie.id == filme_id).update(request.dict())
    db.commit()

    return "Filme atualizado com sucesso!"
