#from department_app.models.department_model import Department
from .serializer import ma
from .employee_serializer import EmployeeSchema
from marshmallow import fields

class DepartmentSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)

