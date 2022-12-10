from flask import Flask


def register_api_blueprints(app: Flask):
    ...


def register_flask_plugins(app: Flask):
    ...


def create_app() -> Flask:
    app = Flask(__name__)
    return app

