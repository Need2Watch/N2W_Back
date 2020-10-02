from passlib.hash import sha256_crypt


class Password():

    # TODO check if str passed is sha256_crypt
    def __init__(self, password: str):
        self.__value = password

    @staticmethod
    def from_string(password: str):
        return Password(sha256_crypt.hash(password))

    @property
    def value(self):
        return self.__value

    def verify(self, password: str) -> bool:
        return sha256_crypt.verify(password, self.__value)
