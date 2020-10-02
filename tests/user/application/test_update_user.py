import uuid
from typing import Optional

import pytest
from faker import Faker

from ....src.user.application.update_user import UpdateUser
from ....src.user.domain.non_existing_user_with_id_error import NonExistingUserWithIdError
from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....tests.user.infrastructure.user_in_memory_repository import UserInMemoryRepository
from ..builder.user_builder import UserBuilder

fake = Faker()


class TestUpdateUser():

    def test_user_is_updated(self):
        user_id = UserId.from_string(str(uuid.uuid4()))
        existing_user = UserBuilder().with_user_id(user_id).build()
        user_repository = UserInMemoryRepository()
        user_repository.save(existing_user)
        updated_user_request = {
            "username": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "city": fake.city()
        }
        update_user_use_case = UpdateUser(user_repository)

        update_user_use_case.run(user_id.value, updated_user_request)

        updated_user: Optional[User] = user_repository.find(existing_user.user_id)
        assert updated_user.username == updated_user_request["username"]
        assert updated_user.first_name == updated_user_request["first_name"]
        assert updated_user.last_name == updated_user_request["last_name"]
        assert updated_user.country == updated_user_request["country"]
        assert updated_user.city == updated_user_request["city"]

    def test_not_existing_user_with_given_id_throws_an_error(self):
        non_existing_user_id = str(uuid.uuid4())
        updated_user_request = {
            "username": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "city": fake.city()
        }

        user_repository = UserInMemoryRepository()
        update_user_use_case = UpdateUser(user_repository)

        with pytest.raises(NonExistingUserWithIdError):
            update_user_use_case.run(non_existing_user_id, updated_user_request)
