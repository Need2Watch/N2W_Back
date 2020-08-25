from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request

from ..repository.movie_repository import MovieRepository
from .service.from_movie_to_dict import FromMovieToDict

from ...user.domain.user_id import UserId

movies = Blueprint("movies", __name__, url_prefix="/movies")


@movies.route('/<int:movie_id>', methods=["GET"])
@movies.route('/<int:movie_id>/<string:user_id>', methods=["GET"])
def get_movie(movie_id: int, user_id: str = None):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id) if user_id else None
    movie = movie_repository.getById(movie_id, user_id)
    if not movie:
        abort(404)

    return jsonify(FromMovieToDict.with_movie(movie))


@movies.route('/popular', methods=["GET"])
@movies.route('/popular/<string:user_id>', methods=["GET"])
def get_popular_movies(user_id: str = None):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id) if user_id else None
    movies = movie_repository.getPopularMovies(user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/top', methods=["GET"])
@movies.route('/top/<string:user_id>', methods=["GET"])
def get_top_movies(user_id: str = None):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id) if user_id else None
    movies = movie_repository.getTopRated(user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/similar/<int:movie_id>', methods=["GET"])
@movies.route('/similar/<int:movie_id>/<string:user_id>', methods=["GET"])
def get_similar_movies(movie_id: int, user_id: str = None):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id) if user_id else None
    movies = movie_repository.getSimilarById(movie_id, user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/following/<string:user_id>', methods=["GET"])
def get_following_movies(user_id: str):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id)
    movies = movie_repository.get_following_movies(user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/watched/<string:user_id>', methods=["GET"])
def get_watched_movies(user_id: str):
    movie_repository = MovieRepository()
    user_id = UserId.from_string(user_id)
    movies = movie_repository.get_watched_movies(user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/search', methods=["POST"])
def search_movie(user_id: str = None):
    movie_repository = MovieRepository()

    title = request.json.get('title')
    user_id = request.json.get('user_id', None)
    user_id = UserId.from_string(user_id) if user_id else None

    movies = movie_repository.getByTitle(title, user_id)
    if not movies:
        abort(404)

    return jsonify(list(map(lambda movie: FromMovieToDict.with_movie(movie), movies)))


@movies.route('/follow', methods=["POST"])
def follow_movie():
    movie_repository = MovieRepository()

    movie_id = request.json.get('movie_id')
    user_id = request.json.get('user_id')

    user_id = UserId.from_string(user_id)
    movie_repository.follow_movie(user_id, movie_id)

    return '200'


@movies.route('/unfollow', methods=["POST"])
def unfollow_movie():
    movie_repository = MovieRepository()

    movie_id = request.json.get('movie_id')
    user_id = request.json.get('user_id')

    user_id = UserId.from_string(user_id)
    movie_repository.unfollow_movie(user_id, movie_id)

    return '200'


@movies.route('/watch', methods=["POST"])
def watch_movie():
    movie_repository = MovieRepository()

    movie_id = request.json.get('movie_id')
    user_id = request.json.get('user_id')

    user_id = UserId.from_string(user_id)
    movie_repository.watch_movie(user_id, movie_id)

    return '200'


@movies.route('/unwatch', methods=["POST"])
def unwatch_movie():
    movie_repository = MovieRepository()

    movie_id = request.json.get('movie_id')
    user_id = request.json.get('user_id')

    user_id = UserId.from_string(user_id)
    movie_repository.unwatch_movie(user_id, movie_id)

    return '200'
