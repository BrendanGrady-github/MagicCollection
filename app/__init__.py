from flask import Flask
from config import Config
from app.models import db, CollectionEntry, Storage, StorageSection


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app