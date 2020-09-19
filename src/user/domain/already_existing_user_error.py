class AlreadyExistingUserError(Exception):
    def __init__(self, user_email: str):
        self.message = 'User with email: {0} already exists'.format(user_email)

    def __str__(self):
        return self.message
