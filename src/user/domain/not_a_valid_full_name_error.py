class NotAValidFullNameError(Exception):
    def __init__(self, first_name: str, last_name: str):
        self.message = 'Fullname: {0} {1} is not a valid full name.'.format(first_name, last_name)

    def __str__(self):
        return self.message
