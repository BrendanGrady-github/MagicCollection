from flask import Flask
from app.models import db


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app