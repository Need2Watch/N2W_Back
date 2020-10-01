import pytest
from faker import Faker

from ....src.user.domain.email import Email
from ....src.user.domain.not_a_valid_email_error import NotAValidEmailError

fake = Faker()


class TestEmail():
    def test_valid_email_should_be_constructed(self):
        valid_email = fake.email()
        email = Email.from_string(valid_email)
        assert email.value == valid_email

    def test_not_valid_email_should_raise_a_NotAValidEmailError(self):
        not_valid_email = fake.word()
        with pytest.raises(NotAValidEmailError):
            Email.from_string(not_valid_email)
