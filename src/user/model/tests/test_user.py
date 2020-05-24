import unittest
import json
import uuid
from faker import Faker
from ..user import User
from ..user_id import UserId

fake = Faker(['es_ES', 'it_IT'])


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user_id = UserId(uuid.uuid4())
        username = fake.name()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        country = fake.country()
        city = fake.city()
        favourite_genres = ["Thriller", "Adventure", "Comedy"]

        user = User(user_id, username, password, first_name, last_name,
                    email, country, city, favourite_genres)

        self.assertEqual(type(user), User)

    def test_user_from_json(self):
        frontend_json_dict = {
            'user_id': str(uuid.uuid4()),
            'username': fake.name(),
            'password': fake.password(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'country': fake.country(),
            'city': fake.city(),
            'favourite_genres': ["Thriller", "Adventure", "Comedy"]
        }
        frontend_user_json = json.dumps(frontend_json_dict)

        user = User.from_json(frontend_user_json)

        self.assertEqual(type(user), User)

    def test_user_to_json(self):
        user_id = UserId(uuid.uuid4())
        username = fake.name()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        country = fake.country()
        city = fake.city()
        favourite_genres = ["Thriller", "Adventure", "Comedy"]

        user = User(user_id, username, password, first_name, last_name,
                    email, country, city, favourite_genres)
        backend_json = user.to_json()

        expected_value = json.dumps({
            'user_id': str(user_id.value),
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'country': country,
            'city': city,
            'favourite_genres': favourite_genres
        })
        self.assertEqual(backend_json, expected_value)
