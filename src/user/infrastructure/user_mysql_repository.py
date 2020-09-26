import os
from typing import Optional

import sqlalchemy as db

from ..domain.password import Password
from ..domain.user import User
from ..domain.user_id import UserId
from ..domain.user_repository import UserRepository


class UserMysqlRepository(UserRepository):

    def __init__(self):
        self.__db_engine = db.create_engine(os.getenv('DB_ENGINE'))
        self.__db_connection = self.__db_engine.connect()
        self.__db_metadata = db.MetaData()
        self.__users = db.Table("users", self.__db_metadata, autoload=True, autoload_with=self.__db_engine)

    def save(self, user: User):
        query = db.insert(self.__users).values(
            user_id=user.user_id.value,
            username=user.username,
            password=user.password.value,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            country=user.country,
            city=user.city
        )

        self.__db_connection.execute(query)

    def delete(self, user: User):
        query = db.delete(self.__users).where(
            self.__users.columns.user_id == user.user_id.value)
        self.__db_connection.execute(query)

    def update(self, user: User):
        query = db.update(self.__users).values(
            user_id=user.user_id.value,
            username=user.username,
            password=user.password.value,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            country=user.country,
            city=user.city
        ).where(self.__users.columns.user_id == user.user_id.value)

        self.__db_connection.execute(query)

    def find(self, user_id: UserId) -> Optional[User]:
        query = db.select([self.__users]).where(self.__users.columns.user_id == user_id.value)
        resultProxy = self.__db_connection.execute(query)

        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None

        return self.__getUserFromResult(resultSet[0])

    def find_by_email(self, email):
        query = db.select([self.__users]).where(
            self.__users.columns.email == email)
        resultProxy = self.__db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return self.__getUserFromResult(resultSet[0])

    def __getUserFromResult(self, result: tuple):
        return User(
            user_id=UserId.from_string(result[0]),
            username=result[1],
            password=Password(result[2]),
            first_name=result[3],
            last_name=result[4],
            email=result[5],
            country=result[6],
            city=result[7]
        )
