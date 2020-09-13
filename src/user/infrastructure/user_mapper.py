from ..domain.password import Password
from ..domain.user import User
from ..domain.user_id import UserId
from .user_dto import UserDTO


class UserMapper:
    @staticmethod
    def from_dto_to_aggregate(user_dto: UserDTO) -> User:
        return User(
            user_id=UserId.from_string(user_dto['user_id']),
            username=user_dto['username'],
            password=Password.from_string(user_dto['password']),
            first_name=user_dto['first_name'],
            last_name=user_dto['last_name'],
            email=user_dto['email'],
            country=user_dto['country'],
            city=user_dto['city']
        )

    @staticmethod
    def from_aggregate_to_dto(user: User) -> UserDTO:
        return UserDTO(
            user_id=user.user_id.value,
            email=user.email,
            password=user.password.value,
            username=user.username,
            profile_picture=user.profile_picture,
            first_name=user.first_name,
            last_name=user.last_name,
            country=user.country,
            city=user.city
        )
