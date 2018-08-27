from flask import Flask
from .sentiment_api import SentimentApi

sentiment_api = SentimentApi()

def create_app():
    app = Flask(__name__)
    sentiment_api.init_app(app)

    from .api import rest_api as api_blue_print
    app.register_blueprint(api_blue_print, url_prefix='/api')
    
    return app