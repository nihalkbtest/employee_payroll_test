from models import db

class Leave(db.Model):
    __tablename__ = 'leaves'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    leave_type = db.Column(db.String(50))  # Sick, Casual, etc.
    status = db.Column(db.String(50), default='Pending')

    # Relationship with Employee
    employee = db.relationship('Employee', back_populates='leaves')

    def __repr__(self):
        return f"<Leave {self.leave_type} - Status: {self.status}>"
