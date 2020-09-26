from .user_id import UserId


class NoExistingUserWithIdError(Exception):
    def __init__(self, user_id: UserId):
      self.message = 'User with id: {0} does not exist'.format(user_id)

    def __str__(self):
        return self.message