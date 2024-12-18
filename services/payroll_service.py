from models.payroll import Payroll
from models.employee import Employee
from datetime import datetime
from sqlalchemy.orm import joinedload
from models import db 

def calculate_payroll(employee_id):
    # Fetch the employee details and payroll data
    employee = Employee.query.filter_by(id=employee_id).first()

    if not employee:
        return None, "Employee not found"

    # Basic salary logic (you can extend it as per your rules)
    salary = employee.salary  # You could also add logic here to calculate based on hours worked, etc.

    # Example: Fetch payroll data and calculate deductions, bonuses, etc.
    payroll = Payroll.query.filter_by(employee_id=employee_id).order_by(Payroll.date.desc()).first()

    if payroll:
        deductions = payroll.deductions
        bonuses = payroll.bonuses
    else:
        deductions = 0
        bonuses = 0

    # Calculate net salary
    net_salary = salary + bonuses - deductions

    return {
        "employee_name": employee.name,
        "salary": salary,
        "deductions": deductions,
        "bonuses": bonuses,
        "net_salary": net_salary,
        "payroll_date": datetime.now().strftime("%Y-%m-%d")
    }

def add_payroll_entry(employee_id, salary, bonuses=0, deductions=0):
    # Add a payroll entry for the employee
    payroll_entry = Payroll(employee_id=employee_id, salary=salary, bonuses=bonuses, deductions=deductions, date=datetime.now())
    db.session.add(payroll_entry)
    db.session.commit()
    return payroll_entry
