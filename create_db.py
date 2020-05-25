import sqlalchemy as db
import os
from uuid import UUID

engine = db.create_engine(os.environ["DB_ENGINE"])
connection = engine.connect()
metadata = db.MetaData()


def create_user_table():
    users = db.Table('users', metadata,
                db.Column('userid', db.String(36), nullable=False),
                db.Column('username', db.String(255), nullable=False),
                db.Column('password', db.String(255), nullable=False),
                db.Column('first_name', db.String(255), nullable=False),
                db.Column('last_name', db.String(255), nullable=False),
                db.Column('email', db.String(255), nullable=False),
                db.Column('country', db.String(255), nullable=False),
                db.Column('city', db.String(255), nullable=False),
            )     
    

if __name__ == "__main__":
    create_user_table()
    metadata.create_all(engine)