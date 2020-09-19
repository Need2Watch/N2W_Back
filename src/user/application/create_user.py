from ..domain.already_existing_user_error import AlreadyExistingUserError
from ..domain.password import Password
from ..domain.user import User
from ..domain.user_id import UserId
from ..domain.user_repository import UserRepository
from .user_dto import UserDTO


class CreateUser():
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def run(self, user_dto: UserDTO):
        user = User(
            user_id=UserId.from_string(user_dto['user_id']),
            username=user_dto['username'],
            password=Password.from_string(user_dto['password']),
            first_name=user_dto['first_name'],
            last_name=user_dto['last_name'],
            email=user_dto['email'],
            country=user_dto['country'],
            city=user_dto['city']
        )

        if self.__user_repository.find_by_email(user.email):
            raise(AlreadyExistingUserError(user.email))

        self.__user_repository.save(user)
