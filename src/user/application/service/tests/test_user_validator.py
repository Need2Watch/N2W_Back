import unittest
import uuid
from faker import Faker

from ..user_validator import UserValidator

fake = Faker(['es_ES', 'it_IT'])

class TestUserValidator(unittest.TestCase):

    def test_correct_case(self):
        user = {
            "user_id": str(uuid.uuid4()),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.name(),
            "password": fake.password(),
            "city": fake.city(),
            "country": fake.country(),
            "email": fake.email(),
        }

        self.assertTrue(UserValidator().validate_user(user))

    
    def test_bad_case_not_completed(self):
        user = {
            "user_id": str(uuid.uuid4()),
            "first_name": fake.first_name(),
            "city": fake.city(),
            "country": fake.country(),
            "email": fake.email(),
        }

        self.assertFalse(UserValidator().validate_user(user))


    def test_bad_case_not_correct_type(self):
        user = {
            "user_id": str(uuid.uuid4()),
            "first_name": 8989,
            "last_name": fake.last_name(),
            "username": 89890,
            "password": fake.password(),
            "city": fake.city(),
            "country": fake.country(),
            "email": fake.email(),
        }

        self.assertFalse(UserValidator().validate_user(user))
