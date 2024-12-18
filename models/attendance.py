from models import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    date = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(10))  # Present, Absent, Leave

    employee = db.relationship('Employee', backref='attendance')

    def __repr__(self):
        return f"<Attendance EmployeeID: {self.employee_id} Status: {self.status}>"