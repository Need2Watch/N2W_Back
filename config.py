class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
}
