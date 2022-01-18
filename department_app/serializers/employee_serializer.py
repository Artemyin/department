from marshmallow import fields, validates, ValidationError, validate, post_load

from . import ma

from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


class DepartmentField(fields.Nested):
    """Inherit neseted field for change deserealiaztion(load)
    behavior. because _schema error. 

    :param fields: [description]
    :type fields: [type]
    """
    def _deserialize(self, value, attr, data, partial=None, **kwargs):
        return value
    
      
class EmployeeSchema(ma.Schema):
    class Meta:
        model = Employee                      
        dateformat = '%Y-%m-%d' 

    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=2))
    birthdate = fields.Date()
    salary = fields.Integer(validate=validate.Range(min=0))
    department = DepartmentField("DepartmentSchema", only=("id", "name"), required=False, 
        allow_none=True, default=None, )

    @validates("name")
    def is_name_exist(self, name):
        query = Employee.query.filter(Employee.name.like(f'%{name}%')).all()
        if name.lower() in [employee.name.lower() for employee in query]:
            raise ValidationError("This name already exist in DB")

    @validates("id")
    def is_id_exist(self, id):
        if not Employee.query.filter_by(id=id).all():
            raise ValidationError("There is no id in DB")

    @validates("department")
    def is_department_exist(self, id):
        if not Department.query.filter_by(id=id).all():
            raise ValidationError("There is no department id in DB")

    @post_load
    def make_employee(self, data, **kwargs):
        return Employee(**data)
               