from faker import Faker
import uuid

from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.infrastructure.user_repository_double import UserRepositoryDouble
from ....src.user.application.create_user import CreateUser

faker = Faker()


class TestCreateUser():
    def test_new_user_is_created(self):
        user_repository = UserRepositoryDouble()
        use_case: CreateUser = CreateUser(user_repository)
        user = a_non_existing_user()

        use_case.run(user)

        user_id = UserId.from_string(user['user_id'])
        found_user = user_repository.find(user_id)
        assert found_user != None
        assert_user(found_user, user)

    def test_already_existing_user_throws_an_error(self):
        pass


def a_non_existing_user():
    return {
        'user_id': str(uuid.uuid4()),
        'username': faker.name(),
        'password': faker.password(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'country': faker.country(),
        'city': faker.city()
    }


def assert_user(found_user: User, user):
    assert str(found_user.user_id.value) == user['user_id']
    assert found_user.username == user['username']
    assert found_user.email == user['email']
