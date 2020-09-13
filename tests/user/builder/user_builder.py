import uuid

from faker import Faker

from ....src.user.domain.password import Password
from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.infrastructure.user_dto import UserDTO
from ....src.user.infrastructure.user_mapper import UserMapper

fake = Faker()


class UserBuilder():
    def __init__(self):
        self.__user_id: UserId = UserId.from_string(str(uuid.uuid4()))
        self.__username = fake.name()
        self.__password: Password = Password.from_string(fake.password())
        self.__first_name = fake.first_name()
        self.__last_name = fake.last_name()
        self.__email = fake.email()
        self.__country = fake.country()
        self.__city = fake.city()

    def with_user_id(self, user_id: str):
        self.__user_id = UserId.from_string(user_id)
        return self

    def with_email(self, email: str):
        self.__email = email
        return self

    def build(self) -> User:
        return User(
            self.__user_id,
            self.__username,
            self.__password,
            self.__first_name,
            self.__last_name,
            self.__email,
            self.__country,
            self.__city
        )

    def build_dto(self) -> UserDTO:
        user = self.build()
        return UserMapper().from_aggregate_to_dto(user)
