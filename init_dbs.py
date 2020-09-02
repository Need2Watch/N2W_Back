import sqlalchemy as db
import os
from uuid import UUID

engines = {
    'database': db.create_engine(os.getenv("DB_ENGINE")),
    'test_database': db.create_engine(os.getenv("DB_ENGINE_TEST"))
}
metadata = db.MetaData()

def remove_existing_tables(engine):
    sql = 'DROP TABLE IF EXISTS users;DROP TABLE IF EXISTS watched_movies;DROP TABLE IF EXISTS followed_movies;'
    result = engine.execute(sql)

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
    for engine in engines.values():
        remove_existing_tables(engine)

    create_user_table()
    create_watched_movies_table()
    create_following_movies_table()

    for engine in engines.values():
        metadata.create_all(engine)