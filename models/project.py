from models import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='Active')

    # Many-to-Many relationship with Employee
    employees = db.relationship('Employee', secondary='project_employees', back_populates='projects')

    def __repr__(self):
        return f"<Project {self.name}>"

# Association Table for many-to-many relationship between Project and Employee
project_employees = db.Table('project_employees',
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True),
    db.Column('employee_id', db.Integer, db.ForeignKey('employees.id'), primary_key=True)
)
