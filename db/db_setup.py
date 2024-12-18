from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def init_app(app: Flask):
    """Initialize the database and migration with the Flask app."""
    # Bind SQLAlchemy and Migrate to the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Return the database object so it can be used elsewhere
    return db
