from ..model.movie import Movie
from ...user.model.user_id import UserId

from ....config import db_engine, db_metadata, db_connection

from tmdbv3api import TMDb, Movie
import sqlalchemy as db
from sqlalchemy import and_
import uuid

import os

POSTER_URL = "https://image.tmdb.org/t/p/original"


class MovieRepository:

    def __init__(self):
        self.__tmdb = TMDb()
        self.__tmdb.api_key = os.environ['MOVIE_API_KEY']
        self.__tmdb.language = 'en'
        self.__tmdb.debug = True
        self.__movie = Movie()
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
        if not movie_from_api:
            return None
        return self.__getMovieFromApiResult(movie_from_api)

    def __getMovieFromApiResult(self, result: Movie, user_id: UserId = None):
        return Movie(
            movie_id = result.id,
            title = result.title,
            poster_url = POSTER_URL + result.porter_path,
            rating = result.vote_average,
            genres = map(lambda genre: genre["name"], result.genres),
            overview = result.overview,
            following = __is_following(result.id, user_id) if user_id else False,
            watched = __has_watched(result.id, user_id) if user_id else False
        )

    def __is_following(self, movie_id: int, user_id: UserId):
        query = db.select([self.__followed_movies]).where(
                    and_(self.__followed_movies.columns.user_id == user_id, 
                        self.__followed_movies.columns.movie_id == movie_id
                        ) 
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