from ..model.movie import Movie
from ...user.model.user_id import UserId

from ....config import db_engine, db_metadata, db_connection

from tmdbv3api import TMDb
from tmdbv3api import Movie as ApiMovies
import sqlalchemy as db
from sqlalchemy import and_
import uuid
from dotenv import load_dotenv

load_dotenv()

import os

POSTER_URL = "https://image.tmdb.org/t/p/original"


class MovieRepository:

    def __init__(self):
        self.__tmdb = TMDb()
        self.__tmdb.api_key = os.getenv('MOVIE_API_KEY')
        self.__tmdb.language = 'en'
        self.__tmdb.debug = True
        self.__movie = ApiMovies()
        self.__followed_movies = db.Table("followed_movies", db_metadata,
                                autoload=True, autoload_with=db_engine)
        self.__watched_movies = db.Table("watched_movies", db_metadata,
                                autoload=True, autoload_with=db_engine)

    def add(self, movie: Movie):
        pass

    def delete(self, movie: Movie):
        pass

    def update(self, movie: Movie):
        pass

    def getById(self, movie_id: int, user_id: UserId = None):
        movie_from_api = self.__movie.details(movie_id)

        # There are cases where the api returns an object without properties
        # We need to return None in those cases too
        if not movie_from_api or not hasattr(movie_from_api, 'id'):
            return None
        return self.__getMovieFromApiResult(movie_from_api)

    def __getMovieFromApiResult(self, result: Movie, user_id: UserId = None):
        following = self.__is_following(result.id, user_id) if user_id else False
        watched = self.__has_watched(result.id, user_id) if user_id else False
        return Movie(
            movie_id = result.id,
            title = result.title,
            poster_url = POSTER_URL + result.poster_path,
            rating = result.vote_average,
            genres = list(map(lambda genre: genre["name"], result.genres)),
            overview = result.overview,
            following = following,
            watched = watched
        )

    def __is_following(self, movie_id: int, user_id: UserId):
        query = db.select([self.__followed_movies]).where(
                    and_(self.__followed_movies.columns.user_id == user_id,
                        self.__followed_movies.columns.movie_id == movie_id)
                )
        resultProxy = db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return False
        return True

    def __has_watched(self, movie_id: int, user_id: UserId):
        query = db.select([self.__watched_movies]).where(
                    and_(self.__watched_movies.columns.user_id == user_id,
                        self.__watched_movies.columns.movie_id == movie_id
                        )
                )
        resultProxy = db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return False
        return True