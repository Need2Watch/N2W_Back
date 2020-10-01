import re

from .not_a_valid_email_error import NotAValidEmailError


class Email():

    def __init__(self, email: str):
        self.__validate_email(email)
        self.__value: str = email

    @staticmethod
    def from_string(email: str):
        return Email(email)

    @property
    def value(self):
        return self.__value

    def __validate_email(self, email: str):
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise NotAValidEmailError(email)
