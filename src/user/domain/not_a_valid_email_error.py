class NotAValidEmailError(Exception):
    def __init__(self, email: str):
      self.message = '{0} is not a valid email.'.format(email)

    def __str__(self):
        return self.message