from models import db
from department_app.models import Employee, Department


class EmployeeService:

    def get_all():
        employees = Employee.query.all()
        return employees
        pass

    def get_by_parametr(**kwargs):
        pass

    def put(**kwargs):
        pass    

    def path(**kwargs):
        pass

    def add(**kwargs):
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


class DepartmentService:

    def get_all():
        departments = Department.query.all()
        return departments
        pass

    def get_by_param(*kwargs):
        pass

    def add(*kwargs):
        pass

    def delete(*kwargs):
        pass

    def put(*kwargs):
        pass

    def path(*kwargs):
        pass


