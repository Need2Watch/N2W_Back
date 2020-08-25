import unittest
import uuid
from faker import Faker

from ....src.user.infrastructure.login_validator import LoginValidator

fake = Faker(['es_ES', 'it_IT'])

class TestLoginValidator(unittest.TestCase):

    def test_correct_case(self):
        login = {
            "email": fake.email(),
            "password": fake.password(),
        }

        self.assertTrue(LoginValidator().validate_login(login))


    def test_bad_case_not_completed(self):
        login = {
            "email": fake.email()
        }

        self.assertFalse(LoginValidator().validate_login(login))


    def test_bad_case_not_correct_type(self):
        login = {
            "email": 35234,
            "password": fake.password(),
        }

        self.assertFalse(LoginValidator().validate_login(login))