from fastapi import FastAPI
from app.api.routes import movies, actors, genres, genres_in_movie, directors_in_movie, user, autentication, directors, writers, writers_in_movie, actors_in_movie
from app.api.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://172.17.0.1:3000",
    "http://172.17.0.1:8000",
    "http://frontend:3000",
    "http://backend:8000",
]

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

app.include_router(movies.router)
app.include_router(genres.router)
app.include_router(directors.router)
app.include_router(writers.router)
app.include_router(actors.router)
app.include_router(genres_in_movie.router)
app.include_router(directors_in_movie.router)
app.include_router(writers_in_movie.router)
app.include_router(actors_in_movie.router)
app.include_router(user.router)
app.include_router(autentication.router)
