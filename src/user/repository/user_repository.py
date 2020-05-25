from ..model.user import User
from ..model.user_id import UserId
from ..model.password import Password

from ....config import db_engine, db_metadata, db_connection

from uuid import UUID
import sqlalchemy as db


class UserRepository:

    def __init__(self):
        self.__users = db.Table("users", db_metadata,
                                autoload=True, autoload_with=db_engine)

    def add(self, user: User):
        query = db.insert(self.__users).values(user_id=user.user_id, username=user.username,
                                               password=user.password, first_name=user.first_name,
                                               last_name=user.last_name, email=user.email, country=user.country,
                                               city=user.city)
        resultProxy = db_connection.execute(query)

    def delete(self, user: User):
        query = db.delete(self.__users).where(
            self.__users.columns.user_id == user.user_id)
        resultProxy = db_connection.execute(query)

    def update(self, user: User):
        query = db.update(self.__users).values(user_id=user.user_id, username=user.username,
                                               password=user.password, first_name=user.first_name,
                                               last_name=user.last_name, email=user.email, country=user.country,
                                               city=user.city)
        resultProxy = db_connection.execute(query)

    def getById(self, user_id: UUID):
        query = db.select([self.__users]).where(
            self.__users.columns.user_id == user_id)
        resultProxy = db_connection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return self.__getUserFromResult(resultSet[0])

    def getByEmail(self, email):
        query = db.select([self.__users]).where(
            self.__users.columns.email == email)
        resultProxy = db_connection.execute(query)
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
