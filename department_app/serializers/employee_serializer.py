from marshmallow import fields, validates, ValidationError, validate

from . import ma

from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


class EmployeeSchema(ma.Schema):

    class Meta:
        #model = Employee
        dateformat = '%Y-%m-%d'

    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=2))
    birthdate = fields.Date()
    salary = fields.Integer(validate=validate.Range(min=0))
    department = fields.Nested("DepartmentSchema", only=("id", "name"), required=False)
        

    @validates("name")
    def is_name_exist(self, name):
        if Employee.query.filter_by(name=name).all():
            raise ValidationError("This name already exist in DB")

    @validates("id")
    def is_id_exist(self, id):
        if not Employee.query.filter_by(id=id).all():
            raise ValidationError("There is no id in DB")

    # @validates("department")
    # def is_department_exist(self, id):
    #     if not Department.query.filter_by(id=id).all():
    #         raise ValidationError("There is no department id in DB")

