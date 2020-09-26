import json
import time
import uuid
from typing import Optional

from faker import Faker

from ....n2w import app
from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.infrastructure.user_mysql_repository import UserMysqlRepository
from ..builder.user_builder import UserBuilder

fake = Faker()


user_repository = UserMysqlRepository()

user_id = str(uuid.uuid4())
username = fake.name()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
country = fake.country()
city = fake.city()

request_params = {
    "user_id": user_id,
    "username": username,
    "password": password,
    "email": email,
    "first_name": first_name,
    "last_name": last_name,
    "country": country,
    "city": city
}


class TestUsersController():
    def test_users_post(self):
        response = app.test_client().post(
            '/users',
            data=json.dumps(request_params),
            content_type='application/json'
        )

        user_repository = UserMysqlRepository()
        assert response.status_code == 200
        saved_user: Optional[User] = user_repository.find_by_email(email)
        assert saved_user != None
        assert str(saved_user.user_id.value) == user_id
        assert saved_user.email == email

    def test_users_post_returns_409_when_user_already_exists(self):
        response = app.test_client().post(
            '/users',
            data=json.dumps(request_params),
            content_type='application/json'
        )

        assert response.status_code == 409

    def test_users_put(self):
        user_id = UserId.from_string(str(uuid.uuid4()))
        UserBuilder().with_user_id(user_id).insert()
        put_users_request_params = {
            "username": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "city": fake.city()
        }

        response = app.test_client().put(
            '/users/{0}'.format(user_id.value),
            data=json.dumps(put_users_request_params),
            content_type='application/json'
        )

        user_repository = UserMysqlRepository()
        updated_user = user_repository.find(user_id)
        print(updated_user)
        assert response.status_code == 200
        assert updated_user != None
        assert updated_user.username == put_users_request_params["username"]
        assert updated_user.first_name == put_users_request_params["first_name"]
        assert updated_user.last_name == put_users_request_params["last_name"]
        assert updated_user.city == put_users_request_params["city"]
