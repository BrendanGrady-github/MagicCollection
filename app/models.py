from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Storage(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    storage_type = db.Column(db.String(100), nullable=False)

    name = db.Column(db.String(100), nullable=False)

    # Determines whether this storage location is organized
    # into sections (pages, colors, slots, etc.)
    uses_sections = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    sections = db.relationship(
        "StorageSection",
        backref="storage",
        cascade="all, delete-orphan"
    )

class StorageSection(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    storage_id = db.Column(
        db.Integer,
        db.ForeignKey("storage.id"),
        nullable=False
    )


class CollectionEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    scryfall_id = db.Column(db.String(36), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

    # Every card MUST belong to a storage location.
    storage_id = db.Column(
        db.Integer,
        db.ForeignKey("storage.id"),
        nullable=False
    )

    # Some storage locations have sections.
    # Others do not.
    storage_section_id = db.Column(
        db.Integer,
        db.ForeignKey("storage_section.id"),
        nullable=True
    )

    condition = db.Column(
        db.String(50),
        nullable=False,
        default="Near Mint"
    )

    finish = db.Column(
        db.String(50),
        nullable=False,
        default="Nonfoil"
    )

    notes = db.Column(db.String(1000))

    # These relationships let us access the related objects
    # instead of just their database IDs.
    storage = db.relationship("Storage")

    storage_section = db.relationship("StorageSection")