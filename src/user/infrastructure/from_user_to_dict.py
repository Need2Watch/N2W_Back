from ..domain.user import User
from ..domain.user_id import UserId

import json


class FromUserToDict:

    def __init__(self):
        pass

    @staticmethod
    def with_user(user: User):
        user_dict = {
            'user_id': str(user.user_id.value),
            'username': user.username,
            'password': user.password.value,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'profile_picture': user.profile_picture,
            'country': user.country,
            'city': user.city,
        }
        return user_dict
