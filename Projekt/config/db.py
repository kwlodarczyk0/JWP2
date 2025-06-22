import os


class Config:
    """
    Configuration class for Flask application and SQLAlchemy database.

    Attributes:
        SECRET_KEY (str): Secret key for session management and security.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to enable/disable modification tracking.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "secretkey")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://postgres:postgres@localhost:5432/flask_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
