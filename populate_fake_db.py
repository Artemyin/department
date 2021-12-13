import random
import sys
from faker import Faker
from department_app.models.base import db
from department_app.models.employee_model import Employee
from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService
from department_app import create_app

es = EmployeeService()
ds = DepartmentService()

departments = [
    "Management", "Sales", "Engineering", 
    "Service", "HR"
    ]

app = create_app()

def create_fake_users(n):
    """Generate fake users."""
    with app.app_context():
        faker = Faker()
        
        for department in departments:
            print(department)
            dep = ds.add(name=department)

        print(f'Added {len(departments)} departments to the database.')

        for i in range(n):
            emp = Employee(
                name=faker.name(),
                birthdate= faker.date_of_birth(minimum_age=18, maximum_age=60),
                salary=random.randint(100, 1000),
                department=ds.get_by_param(name=random.choice(departments))[0],
            )
            db.session.add(emp)
            print(emp)
        db.session.commit()
        print(f'Added {n} fake users to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument.')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))


