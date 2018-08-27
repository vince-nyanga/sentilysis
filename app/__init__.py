from flask import Flask
from .sentiment_api import SentimentApi
from config import config

sentiment_api = SentimentApi()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    sentiment_api.init_app(app)

    from .main import bp as main_blue_print
    app.register_blueprint(main_blue_print)

    from .api import rest_api as api_blue_print
    app.register_blueprint(api_blue_print, url_prefix='/api')
    
    return app