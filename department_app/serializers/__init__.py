from flask_marshmallow import Marshmallow
ma = Marshmallow()

from .employee_serializer import EmployeeSchema, DepartmentSchema
