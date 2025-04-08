from flask import Flask
from config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    from fvsapi.controller.routes import fvs

    app.register_blueprint(fvs, url_prefix="/fvs")

    return app
