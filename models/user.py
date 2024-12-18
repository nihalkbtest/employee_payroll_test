from models import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'admin' or 'employee'

    # One-to-One relationship with Employee
    employee = db.relationship('Employee', back_populates='user', uselist=False)

    def __repr__(self):
        return f"<User {self.username} - Role: {self.role}>"
