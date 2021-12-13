from marshmallow import fields

from .serializer import ma
from .employee_serializer import EmployeeSchema


class DepartmentSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)

