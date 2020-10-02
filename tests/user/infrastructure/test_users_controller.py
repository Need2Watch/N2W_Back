import json
import uuid
from typing import Optional

from faker import Faker

from ....n2w import app
from ....src.user.domain.user_id import UserId
from ....src.user.infrastructure.user_mysql_repository import UserMysqlRepository
from ..builder.user_builder import UserBuilder

fake = Faker()


def teardown_module():
    UserMysqlRepository().clean()


class TestUsersPostController():
    def test_should_create_and_save_a_user_with_the_passed_parameters(self):
        user_email = fake.email()
        users_post_request_params = get_users_post_request_params_with_email(user_email)

        response = app.test_client().post(
            '/users',
            data=json.dumps(users_post_request_params),
            content_type='application/json'
        )

        user_repository = UserMysqlRepository()
        saved_user = user_repository.find_by_email(user_email)
        assert response.status_code == 200
        assert saved_user != None
        assert saved_user.username == users_post_request_params["username"]
        assert saved_user.password.verify(users_post_request_params["password"])
        assert saved_user.email == users_post_request_params["email"]
        assert saved_user.first_name == users_post_request_params["first_name"]
        assert saved_user.last_name == users_post_request_params["last_name"]
        assert saved_user.city == users_post_request_params["city"]
        assert saved_user.country == users_post_request_params["country"]

    def test_should_return_409_when_creating_a_user_with_an_already_registered_email(self):
        user_email = fake.email()
        UserBuilder().with_email(user_email).insert()
        users_post_request_params = get_users_post_request_params_with_email(user_email)

        response = app.test_client().post(
            '/users',
            data=json.dumps(users_post_request_params),
            content_type='application/json'
        )

        assert response.status_code == 409


def get_users_post_request_params_with_email(email: str):
    return {
        "user_id": str(uuid.uuid4()),
        "username": fake.user_name(),
        "password": fake.password(),
        "email": email,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "country": fake.country(),
        "city": fake.city()
    }


class TestUsersPutController():
    def test_should_update_the_parameters_of_the_user_which_id_is_passed(self):
        user_id = UserId.from_string(str(uuid.uuid4()))
        UserBuilder().with_user_id(user_id).insert()
        users_put_request_params = {
            "username": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "city": fake.city()
        }

        response = app.test_client().put(
            '/users/{0}'.format(user_id.value),
            data=json.dumps(users_put_request_params),
            content_type='application/json'
        )

        user_repository = UserMysqlRepository()
        updated_user = user_repository.find(user_id)
        assert response.status_code == 200
        assert updated_user != None
        assert updated_user.username == users_put_request_params["username"]
        assert updated_user.first_name == users_put_request_params["first_name"]
        assert updated_user.last_name == users_put_request_params["last_name"]
        assert updated_user.city == users_put_request_params["city"]

    def test_should_return_404_when_the_user_to_be_updated_does_not_exist(self):
        non_existing_user_id = str(uuid.uuid4())
        users_put_request_params = {
            "username": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "city": fake.city()
        }

        response = app.test_client().put(
            '/users/{0}'.format(non_existing_user_id),
            data=json.dumps(users_put_request_params),
            content_type='application/json'
        )

        assert response.status_code == 404
