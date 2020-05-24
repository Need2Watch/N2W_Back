import unittest

from ..movie import Movie


class TestMovie(unittest.TestCase):

    def test_constructor(self):
        movie_id = 550
        title = "Fight Club"
        poster_url = "https://image.tmdb.org/t/p/original/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg"
        rating = 8.4
        genres = ["Drama"]
        overview = "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."

        movie = Movie(movie_id, title, poster_url, rating, genres, overview)

        self.assertEqual(type(movie), Movie)
