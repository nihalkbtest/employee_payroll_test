from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.user import User
from models.employee import Employee
from models.attendance import Attendance
from models.project import Project
from models.leave import Leave
from models.education import Education
from utils.decorators import employee_required

employee_bp = Blueprint('employee', __name__)

# Employee Dashboard
@employee_bp.route('/employee/dashboard')
@login_required
@employee_required
def dashboard():
    employee = Employee.query.filter_by(user_id=current_user.id).first()
    if not employee:
        flash("Employee record not found!", "danger")
        return redirect(url_for('auth.login'))

    attendance = Attendance.query.filter_by(employee_id=employee.id).all()
    projects = Project.query.filter_by(employee_id=employee.id).all()
    leaves = Leave.query.filter_by(employee_id=employee.id).all()
    education = Education.query.filter_by(employee_id=employee.id).all()

    return render_template(
        'employee_dashboard.html',
        employee=employee,
        attendance=attendance,
        projects=projects,
        leaves=leaves,
        education=education
    )

# View Attendance Records
@employee_bp.route('/employee/attendance')
@login_required
@employee_required
def view_attendance():
    employee = Employee.query.filter_by(user_id=current_user.id).first()
    if not employee:
        flash("Employee record not found!", "danger")
        return redirect(url_for('employee.dashboard'))

    attendance = Attendance.query.filter_by(employee_id=employee.id).all()
    return render_template('employee_attendance.html', attendance=attendance)

# View Assigned Projects
@employee_bp.route('/employee/projects')
@login_required
@employee_required
def view_projects():
    employee = Employee.query.filter_by(user_id=current_user.id).first()
    if not employee:
        flash("Employee record not found!", "danger")
        return redirect(url_for('employee.dashboard'))

    projects = Project.query.filter_by(employee_id=employee.id).all()
    return render_template('employee_projects.html', projects=projects)

# View Leave Records
@employee_bp.route('/employee/leaves')
@login_required
@employee_required
def view_leaves():
    employee = Employee.query.filter_by(user_id=current_user.id).first()
    if not employee:
        flash("Employee record not found!", "danger")
        return redirect(url_for('employee.dashboard'))

    leaves = Leave.query.filter_by(employee_id=employee.id).all()
    return render_template('employee_leaves.html', leaves=leaves)

# View Education Details
@employee_bp.route('/employee/education')
@login_required
@employee_required
def view_education():
    employee = Employee.query.filter_by(user_id=current_user.id).first()
    if not employee:
        flash("Employee record not found!", "danger")
        return redirect(url_for('employee.dashboard'))

    education = Education.query.filter_by(employee_id=employee.id).all()
    return render_template('employee_education.html', education=education)
