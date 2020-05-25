import unittest
import json
from faker import Faker
import uuid

from ..from_dict_to_user import FromDictToUser
from ....model.user import User
from ....model.password import Password

fake = Faker(['es_ES', 'it_IT'])

class TestFromDictToUser(unittest.TestCase):

    def test_with_dict(self):
        frontend_dict = {
            'user_id': str(uuid.uuid4()),
            'username': fake.name(),
            'password': fake.password(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'country': fake.country(),
            'city': fake.city(),
        }

        user = FromDictToUser.with_dict(frontend_dict)

        self.assertEqual(type(user), User)