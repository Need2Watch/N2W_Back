from ..domain.non_existing_user_with_id_error import NonExistingUserWithIdError
from ..domain.user import User
from ..domain.user_id import UserId
from ..domain.user_repository import UserRepository


class UpdateUser():
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def run(self, str_user_id: str, user_request: dict):
        user_id = UserId.from_string(str_user_id)
        user = self.__user_repository.find(user_id)

        if not user:
            raise(NonExistingUserWithIdError(user_id))

        updated_user = User(
            user.user_id,
            user_request["username"],
            user.password, user_request["first_name"],
            user_request["last_name"],
            user.email,
            user_request["country"],
            user_request["city"]
        )

        self.__user_repository.update(updated_user)
