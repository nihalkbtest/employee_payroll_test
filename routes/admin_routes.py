from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db
from models.user import User
from models.employee import Employee
from models.department import Department
from models.attendance import Attendance
from models.project import Project
from models.education import Education
from models.leave import Leave
from utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

# Admin Dashboard
@admin_bp.route('/admin/dashboard')
@login_required
@admin_required
def dashboard():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('admin_dashboard.html', employees=employees, departments=departments)

# Manage Departments
@admin_bp.route('/admin/departments', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_departments():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_department = Department(name=name, description=description)
        db.session.add(new_department)
        db.session.commit()
        flash('Department added successfully!', 'success')
        return redirect(url_for('admin.manage_departments'))

    departments = Department.query.all()
    return render_template('departments.html', departments=departments)

# Delete Department
@admin_bp.route('/admin/departments/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('Department deleted!', 'danger')
    return redirect(url_for('admin.manage_departments'))

# Manage Attendance
@admin_bp.route('/admin/attendance', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_attendance():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        status = request.form['status']
        new_attendance = Attendance(employee_id=employee_id, status=status)
        db.session.add(new_attendance)
        db.session.commit()
        flash('Attendance recorded successfully!', 'success')
        return redirect(url_for('admin.manage_attendance'))

    attendance = Attendance.query.all()
    employees = Employee.query.all()
    return render_template('attendance.html', attendance=attendance, employees=employees)

# Manage Projects
@admin_bp.route('/admin/projects', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_projects():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        employee_id = request.form['employee_id']

        new_project = Project(name=name, description=description, start_date=start_date,
                              end_date=end_date, employee_id=employee_id)
        db.session.add(new_project)
        db.session.commit()
        flash('Project assigned successfully!', 'success')
        return redirect(url_for('admin.manage_projects'))

    projects = Project.query.all()
    employees = Employee.query.all()
    return render_template('projects.html', projects=projects, employees=employees)

# Manage Leaves
@admin_bp.route('/admin/leaves', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_leaves():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        reason = request.form['reason']
        status = request.form['status']

        new_leave = Leave(employee_id=employee_id, start_date=start_date,
                          end_date=end_date, reason=reason, status=status)
        db.session.add(new_leave)
        db.session.commit()
        flash('Leave record added successfully!', 'success')
        return redirect(url_for('admin.manage_leaves'))

    leaves = Leave.query.all()
    employees = Employee.query.all()
    return render_template('leaves.html', leaves=leaves, employees=employees)

# Manage Education
@admin_bp.route('/admin/education', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_education():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        degree = request.form['degree']
        institution = request.form['institution']
        year_of_completion = request.form['year_of_completion']

        new_education = Education(employee_id=employee_id, degree=degree,
                                  institution=institution, year_of_completion=year_of_completion)
        db.session.add(new_education)
        db.session.commit()
        flash('Education details added successfully!', 'success')
        return redirect(url_for('admin.manage_education'))

    education = Education.query.all()
    employees = Employee.query.all()
    return render_template('education.html', education=education, employees=employees)
