from faker import Faker

from .....src.user.infrastructure.validators.users_put_validator import UsersPutValidator

fake = Faker()


class TestUserValidator():
    def test_correct_case_all_attributes(self):
        user_to_update = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.name(),
            "city": fake.city(),
            "country": fake.country(),
        }

        assert UsersPutValidator().validate(user_to_update) == True

    def test_correct_case_some_attributes(self):
        user_to_update = {
            "username": fake.name(),
            "city": fake.city(),
        }

        assert UsersPutValidator().validate(user_to_update) == True

    def test_bad_case_incorrect_types(self):
        user_to_update = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": [fake.name()],
            "city": 123,
            "country": fake.country(),
        }

        assert UsersPutValidator().validate(user_to_update) == False
