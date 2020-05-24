import os

from flask import Flask
from tmdbv3api import TMDb

from config import config


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


environment = config['development']

tmdb = create_movie_api()
app = create_app(environment)
