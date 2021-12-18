from flask import Flask
from flask_bcrypt import Bcrypt

from .config import config_by_name
from app.main.routes.endpoints import Endpoints
from app.main.routes.errors import ErrorHandler

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app = Endpoints(app).availables()
    ErrorHandler(app).handles()
    flask_bcrypt.init_app(app)
    return app

