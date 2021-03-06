import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'iyihaufewakaizivanekutindakaivigaendefutiuchawacha'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
   
class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
   
config =  {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig

}