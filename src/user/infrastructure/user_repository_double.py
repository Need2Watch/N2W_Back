from typing import List, Optional

from ..domain.user_repository import UserRepository
from ..domain.user import User
from ..domain.user_id import UserId


class UserRepositoryDouble(UserRepository):
    def __init__(self):
        self.__users: List[User] = []

    def save(self, user: User):
        self.__users.append(user)

    def find(self, user_id: UserId) -> Optional[User]:
        for user in self.__users:
            if user.user_id == user_id.value:
                return user
        return None
