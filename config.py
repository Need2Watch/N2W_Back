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

db_engine = db.create_engine(os.getenv('DB_ENGINE'))
db_connection = db_engine.connect()
db_metadata = db.MetaData()
