from typing import TypedDict


class UserDTO(TypedDict):
    user_id: str
    email: str
    password: str
    username: str
    profile_picture: str
    first_name: str
    last_name: str
    country: str
    city: str
