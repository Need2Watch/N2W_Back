from .empty_country_error import EmptyCountryError


class Country():
    def __init__(self, country: str):
        if not country:
            raise EmptyCountryError()
        self.__value = country

    @staticmethod
    def from_string(country: str):
        return Country(country)

    @property
    def value(self):
        return self.__value
