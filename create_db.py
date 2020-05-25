import sqlalchemy as db
import os
from uuid import UUID

engine = db.create_engine(os.environ["DB_ENGINE"])
connection = engine.connect()
metadata = db.MetaData()


def create_user_table():
    users = db.Table('users', metadata,
                db.Column('user_id', db.String(36), nullable=False, primary_key=True),
                db.Column('username', db.String(255), nullable=False),
                db.Column('password', db.String(255), nullable=False),
                db.Column('first_name', db.String(255), nullable=False),
                db.Column('last_name', db.String(255), nullable=False),
                db.Column('email', db.String(255), nullable=False),
                db.Column('country', db.String(255), nullable=False),
                db.Column('city', db.String(255), nullable=False),
            )     

def create_following_movies_table():
    followed_movies = db.Table('followed_movies', metadata,
                db.Column('user_id', db.String(36), nullable=False, primary_key=True),
                db.Column('movie_id', db.Integer(), nullable=False, primary_key=True)
            )  

def create_watched_movies_table():
    watched_movies = db.Table('watched_movies', metadata,
                db.Column('user_id', db.String(36), nullable=False, primary_key=True),
                db.Column('movie_id', db.Integer(), nullable=False, primary_key=True)
            )  

if __name__ == "__main__":
    create_user_table()
    create_watched_movies_table()
    create_following_movies_table()
    metadata.create_all(engine)