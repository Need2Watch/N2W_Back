from abc import ABC, abstractmethod
from .user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    def find_by_email(self, user_email: str):
        pass
