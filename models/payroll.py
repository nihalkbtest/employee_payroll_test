from datetime import datetime
from models import db

class Payroll(db.Model):
    __tablename__ = 'payrolls'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    salary = db.Column(db.Float, nullable=False, default = 10000)
    bonuses = db.Column(db.Float, default=0)
    deductions = db.Column(db.Float, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with Employee
    employee = db.relationship('Employee', back_populates='payroll')

    def __repr__(self):
        return f"<Payroll {self.id} - Employee {self.employee_id}>"
