from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from models import db 

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login Successful!', 'success')
            return redirect(url_for('employee.dashboard'))
        else:
            flash('Login Failed. Check your username and/or password', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful! You can now login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')
