from passlib.hash import sha256_crypt


class Password():

    # TODO check if str passed is sha256_crypt
    def __init__(self, password: str):
        self.__value = password

    @staticmethod
    def fromString(password: str):
        return Password(sha256_crypt.encrypt(password))

    @property
    def value(self):
        return self.__value

    def verify(self, password: str):
        return sha256_crypt.verify(password, self.__value)
