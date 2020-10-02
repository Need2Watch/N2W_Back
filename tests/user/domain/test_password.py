from faker import Faker

from ....src.user.domain.password import Password

fake = Faker()


class TestPassword():
    def test_password_is_not_exposed(self):
        str_password = fake.password()

        password = Password.from_string(str_password)

        assert password.value != str_password

    def test_password_can_be_verified(self):
        str_password = fake.password()

        password = Password.from_string(str_password)

        assert password.verify(str_password) == True
