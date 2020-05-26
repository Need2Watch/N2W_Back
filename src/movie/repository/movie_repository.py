import os
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
        return self.__getMovieFromApiResult(movie_from_api, user_id)

    def getPopularMovies(self, user_id: UserId = None):
        movies_from_api = self.__movie.popular()
        if not movies_from_api:
            return None
        movies = []
        for movie_from_api in movies_from_api:
            # Some details (as genres) are not included when making the popular query
            # So we have to make details query for each movie
            movie = self.__movie.details(movie_from_api.id)
            movies.append(self.__getMovieFromApiResult(movie, user_id))
        return movies

    def getByTitle(self, title: str, user_id: UserId = None):
        movies_from_api = self.__movie.search(title)
        if not movies_from_api:
            return None
        movies = []
        for movie_from_api in movies_from_api:
            # Some details (as genres) are not included when making the search query
            # So we have to make details query for each movie
            movie = self.__movie.details(movie_from_api.id)
            movies.append(self.__getMovieFromApiResult(movie, user_id))
        return movies

    def getSimilarById(self, movie_id: int, user_id: UserId = None):
        # When the movie_id is a 404 in the api tmdbv3api returns an error
        # So we have to force the 404 in that case
        try:
            movies_from_api = self.__movie.similar(movie_id)
        except Exception as e:
            return None

        if not movies_from_api:
            return None
        movies = []
        for movie_from_api in movies_from_api:
            # Some details (as genres) are not included when making the similar query
            # So we have to make details query for each movie
            movie = self.__movie.details(movie_from_api.id)
            movies.append(self.__getMovieFromApiResult(movie, user_id))
        return movies

    def follow_movie(self, user_id: UserId, movie_id: int):
        if self.__is_following(movie_id, user_id):
            return False
        query = db.insert(self.__followed_movies).values(
            user_id=user_id.value, movie_id=movie_id)
        resultProxy = db_connection.execute(query)

    def unfollow_movie(self, user_id: UserId, movie_id: int):
        if not self.__is_following(movie_id, user_id):
            return False
        query = db.delete(self.__followed_movies).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = db_connection.execute(query)

    def watch_movie(self, user_id: UserId, movie_id: int):
        if self.__has_watched(movie_id, user_id):
            return False
        query = db.insert(self.__watched_movies).values(
            user_id=user_id.value, movie_id=movie_id)
        resultProxy = db_connection.execute(query)

    def unwatch_movie(self, user_id: UserId, movie_id: int):
        if not self.__has_watched(movie_id, user_id):
            return False
        query = db.delete(self.__watched_movies).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = db_connection.execute(query)

    def __getMovieFromApiResult(self, result: Movie, user_id: UserId = None):
        following = self.__is_following(
            result.id, user_id) if user_id else False
        watched = self.__has_watched(result.id, user_id) if user_id else False
        poster = (POSTER_URL + result.poster_path) if result.poster_path else ""
        return Movie(
            movie_id=result.id,
            title=result.title,
            poster_url=poster,
            rating=result.vote_average,
            genres=list(map(lambda genre: genre["name"], result.genres)),
            overview=result.overview,
            following=following,
            watched=watched
        )

    def __is_following(self, movie_id: int, user_id: UserId):
        query = db.select([self.__followed_movies]).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return False
        return True

    def __has_watched(self, movie_id: int, user_id: UserId):
        query = db.select([self.__watched_movies]).where(
            and_(self.__watched_movies.columns.user_id == user_id.value,
                 self.__watched_movies.columns.movie_id == movie_id
                 )
        )
        resultProxy = db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return False
        return True
