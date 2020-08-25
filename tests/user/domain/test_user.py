import unittest
import json
import uuid
from faker import Faker
from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.domain.password import Password

fake = Faker(['es_ES', 'it_IT'])


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user_id = UserId(uuid.uuid4())
        username = fake.name()
        password = Password.from_string(fake.password())
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        country = fake.country()
        city = fake.city()

        user = User(user_id, username, password, first_name, last_name,
                    email, country, city)

        self.assertEqual(user.user_id, user_id.value)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password.value)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.country, country)
        self.assertEqual(user.city, city)
