from . import ma
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee

class DepartmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Department

    id = ma.auto_field()
    name = ma.auto_field()
    employee = ma.auto_field()


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True
        
    id = ma.auto_field()
    name = ma.auto_field()
    salary = ma.auto_field()
        

