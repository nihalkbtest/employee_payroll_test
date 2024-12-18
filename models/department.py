from models import db

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))

    # One-to-Many relationship with Employee
    employees = db.relationship('Employee', back_populates='department')

    def __repr__(self):
        return f"<Department {self.name}>"
