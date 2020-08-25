from ..domain.user_repository import UserRepository
from ..domain.user import User
from ..domain.user_id import UserId


class CreateUser():
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def run(self, user):
        user = User(
            user_id=UserId.from_string(user['user_id']),
            username=user['username'],
            password=user['password'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            email=user['email'],
            country=user['country'],
            city=user['city']
        )

        self.__user_repository.save(user)
