from flask import Blueprint

rest_api = Blueprint("api", __name__)

from . import views