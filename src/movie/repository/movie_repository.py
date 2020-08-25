import os
from ..model.movie import Movie
from ...user.domain.user_id import UserId

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
        self.__db_engine = db.create_engine(os.getenv('DB_ENGINE'))
        self.__db_connection = self.__db_engine.connect()
        self.__db_metadata = db.MetaData()
        self.__followed_movies = db.Table("followed_movies", self.__db_metadata,
                                          autoload=True, autoload_with=self.__db_engine)
        self.__watched_movies = db.Table("watched_movies", self.__db_metadata,
                                         autoload=True, autoload_with=self.__db_engine)

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
            movies.append(self.__getMovieFromApiResult(
                movie_from_api, user_id))
        return movies

    def getTopRated(self, user_id: UserId = None):
        movies_from_api = self.__movie.top_rated()
        if not movies_from_api:
            return None
        movies = []
        for movie_from_api in movies_from_api:
            movies.append(self.__getMovieFromApiResult(
                movie_from_api, user_id))
        return movies

    def getByTitle(self, title: str, user_id: UserId = None):
        movies_from_api = self.__movie.search(title)
        if not movies_from_api:
            return None
        movies = []
        for movie_from_api in movies_from_api:
            movies.append(self.__getMovieFromApiResult(
                movie_from_api, user_id))
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
            movies.append(self.__getMovieFromApiResult(
                movie_from_api, user_id))
        return movies

    def get_following_movies(self, user_id: UserId):
        query = db.select([self.__followed_movies.columns.movie_id]).where(
            self.__followed_movies.columns.user_id == user_id.value)

        result_proxy = self.__db_connection.execute(query)
        result_set = result_proxy.fetchall()
        following_movies_ids = self.__getMovieIdsFromResult(result_set)

        movies = []
        for following_movie_id in following_movies_ids:
            movies.append(self.getById(following_movie_id, user_id))

        return movies

    def get_watched_movies(self, user_id: UserId):
        query = db.select([self.__watched_movies.columns.movie_id]).where(
            self.__watched_movies.columns.user_id == user_id.value)

        result_proxy = self.__db_connection.execute(query)
        result_set = result_proxy.fetchall()
        watched_movies_ids = self.__getMovieIdsFromResult(result_set)

        movies = []
        for watched_movie_id in watched_movies_ids:
            movies.append(self.getById(watched_movie_id, user_id))

        return movies

    def follow_movie(self, user_id: UserId, movie_id: int):
        if self.__is_following(movie_id, user_id):
            return False
        query = db.insert(self.__followed_movies).values(
            user_id=user_id.value, movie_id=movie_id)
        resultProxy = self.__db_connection.execute(query)

    def unfollow_movie(self, user_id: UserId, movie_id: int):
        if not self.__is_following(movie_id, user_id):
            return False
        query = db.delete(self.__followed_movies).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = self.__db_connection.execute(query)

    def watch_movie(self, user_id: UserId, movie_id: int):
        if self.__has_watched(movie_id, user_id):
            return False
        query = db.insert(self.__watched_movies).values(
            user_id=user_id.value, movie_id=movie_id)
        resultProxy = self.__db_connection.execute(query)

    def unwatch_movie(self, user_id: UserId, movie_id: int):
        if not self.__has_watched(movie_id, user_id):
            return False
        query = db.delete(self.__watched_movies).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = self.__db_connection.execute(query)

    def __getMovieIdsFromResult(self, result: tuple):
        movie_ids = []
        for movie_id_result in result:
            movie_id = movie_id_result[0]
            movie_ids.append(movie_id)

        return movie_ids

    def __getMovieFromApiResult(self, result: Movie, user_id: UserId = None):
        following = False
        watched = False
        if user_id:
            following = self.__is_following(result.id, user_id)
            watched = self.__has_watched(result.id, user_id)

        poster = ""
        if result.poster_path:
            poster = (POSTER_URL + result.poster_path)

        genres = []
        if hasattr(result, "genres"):
            genres = result.genres

        return Movie(
            movie_id=result.id,
            title=result.title,
            poster_url=poster,
            rating=result.vote_average,
            genres=genres,
            overview=result.overview,
            following=following,
            watched=watched
        )

    def __is_following(self, movie_id: int, user_id: UserId):
        query = db.select([self.__followed_movies]).where(
            and_(self.__followed_movies.columns.user_id == user_id.value,
                 self.__followed_movies.columns.movie_id == movie_id)
        )
        resultProxy = self.__db_connection.execute(query)
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
        resultProxy = self.__db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return False
        return True
