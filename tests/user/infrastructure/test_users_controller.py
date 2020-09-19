from typing import Optional
from faker import Faker
import uuid
import json

from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.infrastructure.user_mysql_repository import UserMysqlRepository
from ....n2w import app

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

        assert response.status_code == 200
        saved_user: Optional[User] = user_repository.find_by_email(email)
        assert saved_user != None
        assertUser(saved_user)

    def test_users_post_returns_409_when_user_already_exists(self):
        response = app.test_client().post(
            '/users',
            data=json.dumps(request_params),
            content_type='application/json'
        )

        assert response.status_code == 409



def assertUser(user: User):
    assert str(user.user_id.value) == user_id
    assert user.username == username
    assert user.email == email
