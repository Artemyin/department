#from department_app.models.employee_model import Employee
from . import ma
#from .department_serializer import DepartmentSchema
#from marshmallow_sqlalchemy.fields import Nested
#from flask_marshmallow import Marshmallow
from marshmallow import fields


class EmployeeSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    birthdate = fields.String()
    salary = fields.Integer()
    department = fields.Nested("DepartmentSchema", only=("id", "name"))
        