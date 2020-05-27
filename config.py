import os
import sqlalchemy as db
from dotenv import load_dotenv

load_dotenv()


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
