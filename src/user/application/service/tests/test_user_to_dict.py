import unittest
import json
from faker import Faker
import uuid

from ..from_user_to_dict import FromUserToDict
from ....model.user import User
from ....model.user_id import UserId
from ....model.password import Password
from hashlib import md5

fake = Faker(['es_ES', 'it_IT'])


class TestFromUserToDict(unittest.TestCase):

    def test_with_user(self):
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

        backend_dict = FromUserToDict.with_user(user)

        digest = md5(email.lower().encode('utf-8')).hexdigest()

        expected_value = {
            'user_id': str(user_id.value),
            'username': username,
            'password': password.value,
            'profile_picture': 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, '500'),
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'country': country,
            'city': city
        }
        self.assertEqual(backend_dict, expected_value)
