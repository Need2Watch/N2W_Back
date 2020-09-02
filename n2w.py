from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from .src.user.infrastructure.users_controller import users
from .src.movie.application.movies import movies

app = Flask(__name__)
CORS(app)

# Swagger
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
