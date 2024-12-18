from models import db

class Education(db.Model):
    __tablename__ = 'educations'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    degree = db.Column(db.String(100))
    university = db.Column(db.String(100))
    graduation_year = db.Column(db.Integer)

    # Relationship with Employee
    employee = db.relationship('Employee', back_populates='education')

    def __repr__(self):
        return f"<Education {self.degree} - {self.university}>"
