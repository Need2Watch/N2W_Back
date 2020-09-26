from abc import ABC, abstractmethod
from .user_id import UserId
from .user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    def find(self, user_id: UserId) -> User:
        pass

    def update(self, user: User):
        pass

    def find_by_email(self, user_email: str) -> User:
        pass
