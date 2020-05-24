import unittest
from passlib.hash import sha256_crypt
from ..password import Password

class TestPassword(unittest.TestCase):

    def test_constructor(self):
        password = Password(sha256_crypt.encrypt("password"))
        self.assertTrue(sha256_crypt.verify("password", password.value))

    def test_from_string(self):
        password = Password.fromString("password")
        self.assertTrue(sha256_crypt.verify("password", password.value))

    def test_if_can_verify(self):
        password = Password.fromString("password")
        self.assertTrue(password.verify("password"))
        self.assertFalse(password.verify("notPassword"))