import uuid
from uuid import UUID


class UserId():

    def __init__(self, user_id: str):
        self.__validate_uuid_v4_format(user_id)
        self.__value: str = user_id

    @staticmethod
    def from_string(user_id: str):
        return UserId(user_id)

    @property
    def value(self):
        return self.__value

    def __validate_uuid_v4_format(self, user_id: str):
        uuid_user_id = UUID(user_id)
        if uuid_user_id.version != 4:
            raise TypeError("user_id must be a version 4 uuid")
