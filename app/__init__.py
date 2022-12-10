from flask import Flask


def register_api_blueprints(app: Flask):
    """注册顶层蓝图"""
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix="/v1")


def register_flask_plugins(app: Flask):
    """注册flask扩展插件"""
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object("app.config.prod")

    register_api_blueprints(app)
    register_flask_plugins(app)

    return app

