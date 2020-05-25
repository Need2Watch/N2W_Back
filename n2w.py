import os

from flask import Flask
from .config import config
from tmdbv3api import TMDb
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv

load_dotenv()

from .src.user.application.auth import users


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    return app


def create_movie_api():
    tmdb = TMDb()
    tmdb.api_key = os.getenv('MOVIE_API_KEY')
    tmdb.language = 'en'
    tmdb.debug = True
    return tmdb


environment = config['development']

app = create_app(environment)
tmdb = create_movie_api()

### swagger specific ###
SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Need2Watch REST API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(users)
