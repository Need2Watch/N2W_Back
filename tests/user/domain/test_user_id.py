
import unittest
import uuid
from uuid import UUID
from ....src.user.domain.user_id import UserId


class TestUserId(unittest.TestCase):

    def test_from_string_constructor(self):
        str_user_id = str(uuid.uuid4())
        user_id = UserId.from_string(str_user_id)
        self.assertEqual(user_id.value, str_user_id)

    def test_building_user_id_with_a_non_uuid4_throws_an_error(self):
        str_user_id = str(uuid.uuid1())
        with self.assertRaises(TypeError):
            user_id = UserId(str_user_id)
