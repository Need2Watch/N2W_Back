from ...model.movie import Movie


class FromMovieToDict:

    def __init__(self):
        pass

    @staticmethod
    def with_movie(movie):
        movie_dict = {
            'movie_id' : movie.movie_id,
            'title' : movie.title,
            'poster_url' : movie.poster_url,
            'rating' : movie.rating,
            'genres' : movie.genres,
            'overview' : movie.overview,
            'following': movie.following,
            'watched': movie.watched
        }
        return movie_dict