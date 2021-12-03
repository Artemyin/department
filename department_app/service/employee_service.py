from marshmallow.fields import String
from department_app.models import db
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee

from department_app.service.department_service import DepartmentService


dep_service = DepartmentService()


class EmployeeService:

    def get_all(self):
        employees = Employee.query.all()
        return employees
        pass

    def get_by_param(self, **kwargs):
        parameters = ("id", "name", "birthdate", "salary", "department", "department_id")
        

        if not set(kwargs.keys()).issubset(parameters):
            print("model doesn't have this fields")
            return False
        
        employees = Employee.query.filter_by(**kwargs).all()
        return employees 
        

    def put(self, **kwargs):
        pass    

    def path(self, **kwargs):
        pass

    def add(self, **kwargs):
        instance_parameters = [
            kwargs.get("name"),
            kwargs.get("birthdate"),
            kwargs.get("salary"),
            kwargs.get("department_id"),
        ]
        db.session.add(Employee(*instance_parameters))
        db.session.commit
        pass

    def delete(**kwargs):
        pass

