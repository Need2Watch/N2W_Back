from typing import List, Optional

from ....src.user.domain.user import User
from ....src.user.domain.user_id import UserId
from ....src.user.domain.user_repository import UserRepository


class UserInMemoryRepository(UserRepository):
    def __init__(self):
        self.__users: List[User] = []

    def save(self, user: User):
        self.__users.append(user)

    def update(self, user_to_update: User):
        for user in self.__users:
            if user.user_id.value == user_to_update.user_id.value:
                self.__users.remove(user)
        self.__users.append(user_to_update)

    def find(self, user_id: UserId) -> Optional[User]:
        for user in self.__users:
            if user.user_id.value == user_id.value:
                return user
        return None

    def find_by_email(self, user_email: str) -> Optional[User]:
        for user in self.__users:
            if user.email == user_email:
                return user
        return None