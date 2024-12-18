from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from models import db 

def register_user(username, password):
    # Check if the username is already taken
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return None, "Username is already taken"

    # Create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return new_user, "User registered successfully"

def authenticate_user(username, password):
    # Authenticate user by username and password
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return user, "Login successful"
    return None, "Invalid credentials"

def change_password(user_id, old_password, new_password):
    user = User.query.get(user_id)
    if user and check_password_hash(user.password, old_password):
        user.password = generate_password_hash(new_password, method='sha256')
        db.session.commit()
        return "Password updated successfully"
    return "Old password is incorrect"
