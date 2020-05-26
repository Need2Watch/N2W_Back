from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

from ..repository.movie_repository import MovieRepository
from .service.from_movie_to_dict import FromMovieToDict

movies = Blueprint("movies", __name__, url_prefix="/movies")


@movies.route('/<int:movie_id>', methods=["GET"])
def get_movie(movie_id: int):
    movie_repository = MovieRepository()

    movie = movie_repository.getById(movie_id)
    if not movie:
        abort(404)

    return jsonify(FromMovieToDict.with_movie(movie))


@movies.route('/popular', methods=["GET"])
def get_popular_movies():
    movie_repository = MovieRepository()

    movies = movie_repository.getPopularMovies()
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/similar/<int:movie_id>', methods=["GET"])
def get_similar_movies(movie_id: int):
    movie_repository = MovieRepository()

    movies = movie_repository.getSimilarById(movie_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/search', methods=["POST"])
def search_movie():
    movie_repository = MovieRepository()

    title = request.json.get('title')
    movies = movie_repository.getByTitle(title)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))