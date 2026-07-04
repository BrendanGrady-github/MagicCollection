from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StorageLocation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    storage_type = db.Column(db.String(100), nullable=False)


class CollectionEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    scryfall_id = db.Column(db.String(36), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

    storage_location_id = db.Column(db.Integer, db.ForeignKey("storage_location.id"), nullable=False)

    condition = db.Column(db.String(50), nullable=False, default="Near Mint")

    finish = db.Column(db.String(50), nullable=False, default="Nonfoil")

    notes = db.Column(db.String(1000))

    storage_location = db.relationship("StorageLocation")