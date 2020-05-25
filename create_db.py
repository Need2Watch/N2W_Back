import sqlalchemy as db
import os
from uuid import UUID
from dotenv import load_dotenv

load_dotenv()

engine = db.create_engine(os.getenv("DB_ENGINE"))
connection = engine.connect()
metadata = db.MetaData()

def remove_existing_tables():
    sql = 'DROP TABLE IF EXISTS users;'
    result = engine.execute(sql)

def create_user_table():
    users = db.Table('users', metadata,
                db.Column('user_id', db.String(36), nullable=False),
                db.Column('username', db.String(255), nullable=False),
                db.Column('password', db.String(255), nullable=False),
                db.Column('first_name', db.String(255), nullable=False),
                db.Column('last_name', db.String(255), nullable=False),
                db.Column('email', db.String(255), nullable=False),
                db.Column('country', db.String(255), nullable=False),
                db.Column('city', db.String(255), nullable=False),
            )


if __name__ == "__main__":
    remove_existing_tables()
    create_user_table()
    metadata.create_all(engine)