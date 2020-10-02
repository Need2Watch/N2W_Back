import pytest

from ....src.user.domain.full_name import FullName
from ....src.user.domain.not_a_valid_full_name_error import NotAValidFullNameError


class TestFullName():
    def test_from_string_constructor(self):
        str_full_name = 'John Doe Dio'

        full_name = FullName.from_string(str_full_name)

        assert full_name.first_name == 'John'
        assert full_name.last_name == 'Doe Dio'

    def test_from_first_and_last_name_constructor(self):
        first_name = 'John'
        last_name = 'Doe Dio'

        full_name = FullName.from_first_and_last_name(first_name, last_name)

        assert full_name.value == 'John Doe Dio'

    def test_that_empty_first_or_last_name_raises_a_NotAValidFullNameError(self):
        full_name = ' John '
        first_name = 'J'
        last_name = ' '

        with pytest.raises(NotAValidFullNameError):
            FullName.from_string(full_name)
            FullName.from_first_and_last_name(first_name, last_name)
