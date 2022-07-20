from http.client import HTTPException
from fastapi import APIRouter, Depends, HTTPException, status
from imdb import Cinemagoer
from sqlalchemy import null
from ..schemas.movies import AddMovie
from ..models import Actor, ActorInMovie, Director, DirectorInMovie, GenreInMovie, Movie, Genre, Writer, WriterInMovie
from ..database import get_db
from sqlalchemy.orm import Session

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
def cadastrar_um_novo_filme_com_imdb(imdb_id: str, db: Session = Depends(get_db)):

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

    movie = db.query(Movie.id).filter(Movie.imdb_id == imdb_id).first()

    idMovie = movie.id

    lista_generos = db.query(Genre.name).all()
    lista_diretores = db.query(Director.name).all()
    lista_escritores = db.query(Writer.name).all()
    lista_atores = db.query(Actor.name).all()

    lista_generos = [x[0] for x in lista_generos]
    lista_diretores = [x[0] for x in lista_diretores]
    lista_escritores = [x[0] for x in lista_escritores]
    lista_atores = [x[0] for x in lista_atores]

    for x in imdb_movie['genres']:

        genreName = x

        if genreName not in lista_generos:

            db.add(Genre(name=genreName))
            db.commit()

            genre = db.query(Genre).filter(
                Genre.name == genreName).first()

            idGenre = genre.id

            print(f"O gênero {genreName} foi cadastrado!")

            db.add(GenreInMovie(movie_id=idMovie, genre_id=idGenre))
            db.commit()

            print(
                f"A relação gênero {idGenre} com filme {idMovie} foi cadastrada!")

        else:

            print(f"O gênero {genreName} já está cadastrado!")

            genre = db.query(Genre).filter(
                Genre.name == genreName).first()

            idGenre = genre.id

            db.add(GenreInMovie(movie_id=idMovie, genre_id=idGenre))
            db.commit()

            print(
                f"A relação gênero {idGenre} com filme {idMovie} foi cadastrada!")

    for director in imdb_movie['directors']:

        directorIdImdb = director.personID

        if directorIdImdb is not None:

            person = ia.get_person(directorIdImdb)

            directorName = person['name']

            if directorName not in lista_diretores:

                try:
                    directorHeadshot = person['headshot']
                except:
                    directorHeadshot = "person.png"
                    print(
                        f"Erro ao tentar achar a imagem do diretor {directorName}")

                db.add(Director(name=directorName, headshot=directorHeadshot,
                                id_imdb_director=directorIdImdb))
                db.commit()

                print(f"O diretor {directorName} foi cadastrado!")

                director = db.query(Director).filter(
                    Director.name == directorName).first()

                idDirector = director.id

                db.add(DirectorInMovie(movie_id=idMovie, director_id=idDirector))
                db.commit()

                print(
                    f"A relação diretor {idDirector} com filme {idMovie} foi cadastrada!")

            else:

                print(f"O diretor {directorName} já está cadastrado!")

                director = db.query(Director).filter(
                    Director.name == directorName).first()

                idDirector = director.id

                db.add(DirectorInMovie(movie_id=idMovie, director_id=idDirector))
                db.commit()

                print(
                    f"A relação diretor {idDirector} com filme {idMovie} foi cadastrada!")

    for writer in imdb_movie['writers']:

        writerIdImdb = writer.personID

        if writerIdImdb is not None:

            person = ia.get_person(writerIdImdb)

            writerName = person['name']

            if writerName not in lista_escritores:

                try:
                    writerHeadshot = person['headshot']
                except:
                    writerHeadshot = "person.png"
                    print(
                        f"Erro ao tentar achar a imagem do escritor {writerName}")

                db.add(Writer(name=writerName, headshot=writerHeadshot,
                       id_imdb_writer=writerIdImdb))
                db.commit()

                print(f"O escritor {writerName} foi cadastrado!")

                writer = db.query(Writer).filter(
                    Writer.name == writerName).first()

                idWriter = writer.id

                db.add(WriterInMovie(movie_id=idMovie, writer_id=idWriter))
                db.commit()

                print(
                    f"A relação diretor {idWriter} com filme {idMovie} foi cadastrada!")

            else:

                print(f"O escritor {writerName} já está cadastrado!")

                writer = db.query(Writer).filter(
                    Writer.name == writerName).first()

                idWriter = writer.id

                db.add(WriterInMovie(movie_id=idMovie, writer_id=idWriter))
                db.commit()

                print(
                    f"A relação escritor {idWriter} com filme {idMovie} foi cadastrada!")

    for actor in imdb_movie['actors']:

        actorIdImdb = actor.personID

        if actorIdImdb is not None:

            person = ia.get_person(actorIdImdb)

            actorName = person['name']

            if actorName not in lista_atores:

                try:
                    actorHeadshot = person['headshot']
                except:
                    actorHeadshot = "person.png"
                    print(f"Erro ao tentar achar a imagem do ator {actorName}")

                db.add(Actor(name=actorName, headshot=actorHeadshot,
                       id_imdb_actor=actorIdImdb))
                db.commit()

                print(f"O ator {actorName} foi cadastrado!")

                actor = db.query(Actor).filter(
                    Actor.name == actorName).first()

                idActor = actor.id

                db.add(ActorInMovie(movie_id=idMovie, actor_id=idActor))
                db.commit()

                print(
                    f"A relação ator {idActor} com filme {idMovie} foi cadastrada!")

            else:

                print(f"O ator {actorName} já está cadastrado!")

                actor = db.query(Actor).filter(
                    Actor.name == actorName).first()

                idActor = actor.id

                db.add(ActorInMovie(movie_id=idMovie, actor_id=idActor))
                db.commit()

                print(
                    f"A relação ator {idActor} com filme {idMovie} foi cadastrada!")

    db.refresh(novo_filme)

    return novo_filme


@ router.get('/{filme_id}')
def retornar_filme(filme_id: int, db: Session = Depends(get_db)):

    movie = db.query(Movie).get(filme_id)

    idMovie = movie.id

    genres = db.query(GenreInMovie).filter(
        GenreInMovie.movie_id == idMovie).all()

    directors = db.query(DirectorInMovie).filter(
        DirectorInMovie.movie_id == idMovie).all()

    writers = db.query(WriterInMovie).filter(
        WriterInMovie.movie_id == idMovie).all()

    actors = db.query(ActorInMovie).filter(
        ActorInMovie.movie_id == idMovie).all()

    return movie


@ router.delete('/{filme_id}')
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    db.query(Movie).filter(Movie.id == filme_id).delete(
        synchronize_session=False)
    db.commit()

    return "Filme deletado com sucesso!"


@ router.put('/{filme_id}')
def atualizar_informacoes_do_filme(request: AddMovie, filme_id: int, db: Session = Depends(get_db)):

    db.query(Movie).filter(Movie.id == filme_id).update(request.dict())
    db.commit()

    return "Filme atualizado com sucesso!"
