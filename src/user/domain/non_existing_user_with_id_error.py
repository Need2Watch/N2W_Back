from .user_id import UserId


class NonExistingUserWithIdError(Exception):
    def __init__(self, user_id: UserId):
      self.message = 'User with id: {0} does not exist'.format(user_id.value)

    def __str__(self):
        return self.message