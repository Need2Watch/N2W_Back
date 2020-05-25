import os

from flask import Flask
from .config import config

from .src.user.application.auth import users


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    return app

    
environment = config['development']

app = create_app(environment)

app.register_blueprint(users)
