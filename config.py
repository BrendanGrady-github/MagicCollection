import os


class Config:

    BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # Determine the project's base directory.

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "collection.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False