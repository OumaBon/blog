from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.api_v1 import api
    app.register_blueprint(api)
    return app
