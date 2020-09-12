from hashlib import md5
from .user_id import UserId
from .password import Password


class User:

    def __init__(self, user_id: UserId, username, password: Password, first_name, last_name,
                 email, country, city):
        self.__user_id: UserId = user_id
        self.__username = username
        self.__password: Password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__country = country
        self.__city = city

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

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
    def profile_picture(self, size='500'):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, str(size))

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
