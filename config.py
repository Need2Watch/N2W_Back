import os
import sqlalchemy as db


class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}

db_engine = db.create_engine(os.environ['DB_ENGINE']) 
db_connection = db_engine.connect()
db_metadata = db.MetaData()

