import uuid

import pytest
from faker import Faker

from ....src.user.application.create_user import CreateUser
from ....src.user.domain.already_existing_user_error import AlreadyExistingUserError
from ....src.user.domain.user_id import UserId
from ....src.user.application.user_dto import UserDTO
from ..builder.user_builder import UserBuilder
from ..infrastructure.user_in_memory_repository import UserInMemoryRepository

faker = Faker()

user_repository = UserInMemoryRepository()
use_case: CreateUser = CreateUser(user_repository)
user_id = UserId.from_string(str(uuid.uuid4()))
user_email = faker.email()


class TestCreateUser():

    def test_new_user_is_created(self):
        user_dto: UserDTO = UserBuilder().with_user_id(user_id).with_email(user_email).build_dto()

        use_case.run(user_dto)

        found_user = user_repository.find(user_id)
        assert found_user != None
        assert found_user.user_id.value == user_id.value
        assert found_user.email == user_email

    def test_already_existing_user_throws_an_error(self):
        user_dto: UserDTO = UserBuilder().with_user_id(user_id).with_email(user_email).build_dto()

        with pytest.raises(AlreadyExistingUserError):
            use_case.run(user_dto)
