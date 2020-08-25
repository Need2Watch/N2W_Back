
from cerberus import Validator


class LoginValidator:

    def __init__(self):
        self.__schema = {
            'email': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
        }
        self.__validator = Validator()

    def validate_login(self, login: dict):
        return self.__validator.validate(login, self.__schema)
