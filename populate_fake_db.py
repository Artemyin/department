import random
import sys
from faker import Faker
from marshmallow import ValidationError
from department_app.models.base import db
from department_app.models.employee_model import Employee
from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema
from department_app.serializers.employee_serializer import EmployeeSchema


from department_app import create_app

employee_service = EmployeeService()
department_service = DepartmentService()
employee_schema = EmployeeSchema()
department_schema = DepartmentSchema()

departments = [
    "Management", "Sales", "Engineering", 
    "Service", "HR"
    ]

app = create_app()

def create_fake_users(n):
    """Generate fake users."""
    with app.app_context():
        faker = Faker()
        
        try:
             for department in departments:
                 department = {'name': department}
                 department = department_schema.load(department)
                 department = department_service.create(department=department)
        except ValidationError:
            print(f'{department=} already in db')
            
        print(f'Adpatd {len(departments)} departments to the database.')

        for i in range(n):
            employee = {
                "name": faker.name(),
                "birthdate": faker.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d'),
                "salary": random.randint(100, 1000),
                "department": random.randint(1,5),
            }
            employee = employee_schema.load(employee)
            employee = employee_service.create(employee=employee)

        print(f'Added {n} fake users to the database.')


if __name__ == '__main__':
    # if len(sys.argv) <= 1:
    #     print('Pass the number of users you want to create as an argument.')
    #     sys.exit(1)
    create_fake_users(50)


