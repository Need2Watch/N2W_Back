
from cerberus import Validator


class UserValidator:

    def __init__(self):
        self.__schema = {
            'user_id': {'type': 'string', 'required': True},
            'username': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
            'first_name': {'type': 'string', 'required': True},
            'last_name': {'type': 'string', 'required': True},
            'email': {'type': 'string', 'required': True},
            'country': {'type': 'string', 'required': True},
            'city': {'type': 'string', 'required': True},
        }
        self.__validator = Validator()

    def validate_user(self, user: dict):
        return self.__validator.validate(user, self.__schema)
