from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    """Decorator to restrict access to admin users only."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("You must be an admin to access this page.", "danger")
            return redirect(url_for('auth.login'))  # Redirect to login if not admin
        return f(*args, **kwargs)
    return decorated_function

def employee_required(f):
    """Decorator to restrict access to employee users only."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.is_admin:
            flash("You must be an employee to access this page.", "danger")
            return redirect(url_for('auth.login'))  # Redirect to login if not an employee
        return f(*args, **kwargs)
    return decorated_function
