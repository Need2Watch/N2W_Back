from flask import Flask
from config import config


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    return app


enviroment = config['development']
app = create_app(enviroment)