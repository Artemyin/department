from marshmallow import fields, validates, ValidationError, validate, post_load

from . import ma

from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


class DepartmentField(fields.Nested):
    """Inherit neseted field for change deserealiaztion(load)
    behavior.
    Intend is ommiting missconsisting of Nesting schemas 
    type Department vs type Integer what was cause [_shema] error.
    """
    def _deserialize(self, value, attr, data, partial=None, **kwargs):
        """Deserialization of passed parametr department
        
        :param value: department id
        :type value: int
        """
        return value
    
      
class EmployeeSchema(ma.Schema):
    """Employee Schema for serialization, deserialization, validation
    """
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
    def is_name_exist(self, name: str):
        """Custom field validator for name
        check is id already exist in db

        :param name: employee name
        :type name: str
        :raises ValidationError: This name already exist in DB
        """
        query = Employee.query.filter(Employee.name.like(f'%{name}%')).all()
        if name.lower() in [employee.name.lower() for employee in query]:
            raise ValidationError("This name already exist in DB")

    @validates("id")
    def is_id_exist(self, id: int):
        """Custom field validator for name
        check is name already exist in db

        :param id: employee id
        :type id: int
        :raises ValidationError: There is no id in DB
        """
        if not Employee.query.filter_by(id=id).all():
            raise ValidationError("There is no id in DB")

    @validates("department")
    def is_department_exist(self, department: int):
        """Custom field validator for department
        check is name already exist in db if pased argument is None
        functon return None

        :param id: department id
        :type id: int
        :raises ValidationError: There is no department id in DB
        """
        if id is None:
            return
        if not Department.query.filter_by(id=department).all():
            raise ValidationError("There is no department id in DB")

    @post_load
    def make_employee(self, data, **kwargs):
        """Deserialiaze method for transforming js to ORM object

        :param data: dict with validated parameters
        :type data: dict
        :return: Employee object
        :rtype: Employee
        """
        return Employee(**data)
               