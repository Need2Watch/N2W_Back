import uuid
from uuid import UUID


class UserId():

    def __init__(self, userid: UUID):
        self.checkUniqueId(userid)
        self.checkIdVersion(userid)
        self.__value: UUID = userid

    @staticmethod
    def from_string(userid: str):
        return UserId(UUID(userid))

    @property
    def value(self):
        return self.__value

    def checkUniqueId(self, userid: UUID):
        if type(userid) != UUID:
            raise TypeError("User ID must be an UUID instance")

    def checkIdVersion(self, userid: UUID):
        if userid.version != 4:
            raise TypeError("User ID must be version 4")
