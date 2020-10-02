class EmptyCountryError(Exception):
    def __init__(self):
        self.message = 'User country can not be empty'

    def __str__(self):
        return self.message
