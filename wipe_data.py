import random
import sys
from faker import Faker
from department_app.models.base import db
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee
from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService
from department_app import create_app

es = EmployeeService()
ds = DepartmentService()

app = create_app()

def delete_fake_users():
    """Generate fake users."""
    with app.app_context():
        print("Prepare to delete")
        all_emps = Employee.query.all()
        for emp in all_emps:
            print(f'delete {emp}')
            db.session.delete(emp)
        print(f'deleted all fake users from the database.')

        all_deps = Department.query.all()
        for dep in all_deps:
            print(f'delete {dep}')
            db.session.delete(dep)
        print(f'deleted all fake departments from the database.')

        db.session.commit()
 

if __name__ == '__main__':

    delete_fake_users()


