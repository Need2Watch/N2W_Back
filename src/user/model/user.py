import json
from hashlib import md5
from .user_id import UserId
from .password import Password


class User:

    def __init__(self, user_id: UserId, username, password: Password, first_name, last_name,
                 email, country, city, favourite_genres):
        self.__user_id: UserId = user_id
        self.__username = username
        self.__password: Password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__country = country
        self.__city = city
        self.__favourite_genres = favourite_genres

    @staticmethod
    def from_json(user_json):
        user_dict = json.loads(user_json)
        return User(
            user_id=UserId.from_string(user_dict['user_id']),
            username=user_dict['username'],
            password=user_dict['password'],
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            email=user_dict['email'],
            country=user_dict['country'],
            city=user_dict['city'],
            favourite_genres=user_dict['first_name']
        )

    def to_json(self):
        user_dict = {
            'user_id': str(self.__user_id.value),
            'username': self.__username,
            'password': self.__password,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'email': self.__email,
            'country': self.__country,
            'city': self.__city,
            'favourite_genres': self.__favourite_genres
        }

        user_json = json.dumps(user_dict)
        return user_json

    @property
    def user_id(self):
        return self.__user_id.value

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password.value

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city

    @property
    def favourite_genres(self):
        return self.__favourite_genres

    @property
    def profile_picture(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def verifyPassword(self, password: str):
        return self.__password.verify(password)

    # Flask-login methods
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.__user_id
