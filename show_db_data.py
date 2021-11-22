from department_app import db
from department_app.models import Employee, Department

print("--Employees--")
emps = Employee.query.all()
for emp in emps:
    print(f'{emp.name=}, {emp.salary=}, {emp.department}')

print(' ')
print("--Departments--")
deps = Department.query.all()
for dep in deps:
    print(f'{dep.name=}, {dep.employee=}')

from department_app.service import EmployeeService, DepartmentService

employee_service = EmployeeService
print(employee_service.get_all())

emp_inst = {"name": "Barbara", "birthdate": "10/01/1999", "salary": 200, "department_id": 4}

employee_service.add(**emp_inst)
print(employee_service.get_all())
all_emps = DepartmentService.get_all()
print(all_emps)

from department_app.serializers import EmployeeSchema
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

jsn = employees_schema.dump(all_emps)
print(jsn)