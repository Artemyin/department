from marshmallow import fields

from . import ma



class EmployeeSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    birthdate = fields.String()
    salary = fields.Integer()
    department = fields.Nested("DepartmentSchema", only=("id", "name"))
        