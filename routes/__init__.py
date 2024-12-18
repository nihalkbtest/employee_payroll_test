from flask import Blueprint

# Importing the route files for the application
from .auth import auth_bp
from .admin_routes import admin_bp
from .employee_routes import employee_bp

# Initialize the Blueprint registry
def init_app(app):
    # Register the Blueprints with the Flask app
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(employee_bp, url_prefix='/employee')
