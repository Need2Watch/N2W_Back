from typing import List

from .not_a_valid_full_name_error import NotAValidFullNameError


class FullName():
    def __init__(self, first_name: str, last_name: str):
        first_name.strip()
        last_name.strip()
        if not first_name or not last_name:
            raise NotAValidFullNameError(first_name, last_name)
        self.__first_name = first_name
        self.__last_name = last_name

    @staticmethod
    def from_string(full_name: str):
        splitted_full_name: List[str] = full_name.split(' ', 1)
        first_name = splitted_full_name[0]
        last_name = splitted_full_name[1]
        return FullName(first_name, last_name)

    @staticmethod
    def from_first_and_last_name(first_name: str, last_name: str):
        return FullName(first_name, last_name)

    @property
    def value(self):
        return self.__first_name + ' ' + self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name
