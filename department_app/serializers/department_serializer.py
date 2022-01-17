from marshmallow import fields, validates, ValidationError, post_load

from .serializer import ma
from .employee_serializer import EmployeeSchema

from department_app.models.department_model import Department


class DepartmentSchema(ma.Schema):

    class Meta:
        model = Department

    id = fields.Integer()
    name = fields.String()
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)
    average_salary = fields.Method('calculate_average_salary')

    def calculate_average_salary(self, department):
        try:
            return round(sum(employee.salary for employee in department.employee)/len(department.employee), 2)
        except ZeroDivisionError:
            return 0

    @validates("name")
    def is_name_exist(self, name):
        if Department.query.filter_by(name=name).all():
            raise ValidationError("This name already exist in DB")

    @validates("id")
    def is_id_exist(self, id):
        if not Department.query.filter_by(id=id).all():
            raise ValidationError("There is not id in DB")

    @post_load
    def make_department(self, data, **kwargs):
        return Department(**data)
