from ..domain.user import User
from ..domain.user_id import UserId
from ..domain.password import Password

import json

class FromDictToUser:

    def __init__(self):
        pass

    @staticmethod
    def with_dict(user_dict):
        return User(
            user_id=UserId.from_string(user_dict['user_id']),
            username=user_dict['username'],
            password=Password.from_string(user_dict['password']),
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            email=user_dict['email'],
            country=user_dict['country'],
            city=user_dict['city']
        )
