import os

from flask import Flask
from .config import config
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from .src.user.application.users import users
from .src.user.application.auth import auth
from .src.movie.application.movies import movies


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    return app


environment = config['development']

app = create_app(environment)
CORS(app)
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
app.register_blueprint(movies)
app.register_blueprint(auth)
