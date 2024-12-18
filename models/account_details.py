from models import db

class AccountDetails(db.Model):
    __tablename__ = 'account_details'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    bank_name = db.Column(db.String(100))
    account_number = db.Column(db.String(100))
    account_type = db.Column(db.String(50))

    # Relationship with Employee
    employee = db.relationship('Employee', back_populates='account_details')

    def __repr__(self):
        return f"<AccountDetails {self.bank_name} - {self.account_number}>"
