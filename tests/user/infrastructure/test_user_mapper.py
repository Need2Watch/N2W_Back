from ....src.user.domain.user import User
from ....src.user.infrastructure.user_dto import UserDTO
from ....src.user.infrastructure.user_mapper import UserMapper
from ..builder.user_builder import UserBuilder


class TestUserMapper:

    def test_user_entity_from_user_dto_has_same_attributes(self):
        user_dto: UserDTO = UserBuilder().build_dto()

        user: User = UserMapper().from_dto_to_aggregate(user_dto)

        assert user_dto['user_id'] == user.user_id.value
        assert user_dto['email'] == user.email
        assert user.password.verify(user_dto['password'])
        assert user_dto['username'] == user.username
        assert user_dto['first_name'] == user.first_name
        assert user_dto['last_name'] == user.last_name
        assert user_dto['country'] == user.country
        assert user_dto['city'] == user.city

    def test_user_dto_from_user_entity_has_same_attributes(self):
        user: User = UserBuilder().build()

        user_dto: UserDTO = UserMapper().from_aggregate_to_dto(user)

        assert user_dto['user_id'] == user.user_id.value
        assert user_dto['email'] == user.email
        assert user_dto['password'] == user.password.value
        assert user_dto['username'] == user.username
        assert user_dto['first_name'] == user.first_name
        assert user_dto['last_name'] == user.last_name
        assert user_dto['country'] == user.country
        assert user_dto['city'] == user.city
