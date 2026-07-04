from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(250), nullable=False) # Longest printed Magic card name is currently 141 characters. Using 250 allows room for future cards.

    quantity = db.Column(db.Integer, nullable=False)

    scryfall_id = db.Column(db.String(36), nullable=False)