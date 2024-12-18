# # Initialize the database
# db = db_setup.init_app(app)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin
from config import Config
from models import user 

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Factory function for creating the Flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register blueprints
    from routes.auth import auth_bp
    from routes.admin_routes import admin_bp
    from routes.employee_routes import employee_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(employee_bp, url_prefix='/employee')

    # Define the user_loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        # Assuming you have a User model that can query by id
        return user.User.query.get(int(user_id))

    # Root route
    @app.route('/')
    def home():
        return render_template('index.html')  # Rendering the index.html template

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
