

class Movie:

    def __init__(self, movie_id, title, poster_url, rating, 
                genres, overview, following = False, watched = False):
        self.__movie_id = movie_id
        self.__title = title
        self.__poster_url = poster_url
        self.__rating = rating
        self.__genres = genres
        self.__overview = overview
        self.__following = following
        self.__watched = watched

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def title(self):
        return self.__title

    @property
    def poster_url(self):
        return self.__poster_url
    
    @property
    def rating(self):
        return self.__rating

    @property
    def genres(self):
        return self.__genres

    @property
    def overview(self):
        return self.__overview

    @property
    def following(self):
        return self.__following

    @property
    def watched(self):
        return self.__watched