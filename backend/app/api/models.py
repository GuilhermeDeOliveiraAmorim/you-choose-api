from .database import Base
from sqlalchemy import Float, ForeignKey, String, Column, Integer, Date
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    imdb_id = Column(String)
    title = Column(String)
    year = Column(Integer)
    imdbRating = Column(Float)
    youchooseRating = Column(Float)
    poster = Column(String)


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class GenreInMovie(Base):
    __tablename__ = "genre_in_movie"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey(
        "movies.id", ondelete="SET NULL"), nullable=True)
    genre_id = Column(Integer, ForeignKey(
        "genres.id", ondelete="SET NULL"), nullable=True)

    movie = relationship("Movie", foreign_keys=[movie_id])
    genre = relationship("Genre", foreign_keys=[genre_id])


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class DirectorInMovie(Base):
    __tablename__ = "director_in_movie"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey(
        "movies.id", ondelete="SET NULL"), nullable=True)
    director_id = Column(Integer, ForeignKey(
        "genres.id", ondelete="SET NULL"), nullable=True)

    movie = relationship("Movie", foreign_keys=[movie_id])
    director = relationship("Director", foreign_keys=[director_id])


class Writer(Base):
    __tablename__ = "writers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
