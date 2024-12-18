from models import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    position = db.Column(db.String(100))
    hire_date = db.Column(db.Date)

    # Relationships
    user = db.relationship('User', back_populates='employee')
    department = db.relationship('Department', back_populates='employees')
    education = db.relationship('Education', back_populates='employee')
    projects = db.relationship('Project', secondary='project_employees', back_populates='employees')
    leaves = db.relationship('Leave', back_populates='employee')
    attendance = db.relationship('Attendance', back_populates='employee')
    account_details = db.relationship('AccountDetails', back_populates='employee')
    payroll = db.relationship('Payroll', back_populates='employee')

    def __repr__(self):
        return f"<Employee {self.user_id} Position: {self.position}>"
