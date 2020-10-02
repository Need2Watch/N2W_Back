class City():
    def __init__(self, city: str):
        self.__value = city

    @staticmethod
    def from_string(city: str):
        return City(city)

    @property
    def value(self):
        return self.__value
