from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from typing import Any

db = SQLAlchemy()


class Ship(db.Model):
    """
    SQLAlchemy model representing a ship in the database.

    Attributes:
        id (int): Primary key.
        length (int): Length of the ship.
    """
    id: Any = db.Column(db.Integer, primary_key=True)
    length: Any = db.Column(db.Integer, nullable=False)


class User(UserMixin, db.Model):
    """
    SQLAlchemy model representing a user in the database.

    Attributes:
        id (int): Primary key.
        username (str): Unique username.
        password (str): Hashed password.
    """
    id: Any = db.Column(db.Integer, primary_key=True)
    username: Any = db.Column(db.String(80), unique=True, nullable=False)
    password: Any = db.Column(db.String(200), nullable=False)

