from ...model.user import User
from ...model.user_id import UserId

import json

class FromUserToDict:

    def __init__(self):
        pass

    @staticmethod
    def with_user(user):
        user_dict = {
            'user_id': str(user.user_id),
            'username': user.username,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'country': user.country,
            'city': user.city,
        }
        return user_dict
