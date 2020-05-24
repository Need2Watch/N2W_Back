import os

from flask import Flask
from config import config
from tmdbv3api import TMDb

import sqlalchemy as db


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    return app


def create_movie_api():
    tmdb = TMDb()
    tmdb.api_key = os.environ['MOVIE_API_KEY']
    tmdb.language = 'en'
    tmdb.debug = True
    return tmdb


db_engine = db.create_engine(os.environ['DB_ENGINE'])
db_connection = db_engine.connect()
db_metadata = db.MetaData()

environment = config['development']

tmdb = create_movie_api()
app = create_app(environment)
