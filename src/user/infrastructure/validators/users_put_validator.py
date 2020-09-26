from cerberus import Validator


class UsersPutValidator:
    def __init__(self):
        self.__schema = {
            'username': {'type': 'string', 'required': False},
            'first_name': {'type': 'string', 'required': False},
            'last_name': {'type': 'string', 'required': False},
            'country': {'type': 'string', 'required': False},
            'city': {'type': 'string', 'required': False}
        }
        self.__validator = Validator()

    def validate(self, user: dict):
        return self.__validator.validate(user, self.__schema)
