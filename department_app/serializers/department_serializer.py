from marshmallow import fields, validates, ValidationError, post_load, validate, validates_schema

from .serializer import ma
from .employee_serializer import EmployeeSchema

from department_app.models.department_model import Department


class DepartmentSchema(ma.Schema):
    """Department Schema for serialization, deserialization, validation
    """
    class Meta:
        model = Department

    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=2))
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)
    average_salary = fields.Float(dump_only=True)

    @validates("name")
    def is_name_exist(self, name: str):
        """Custom field validator for name
        check is id already exist in db

        :param name: department name
        :type name: str
        :raises ValidationError: 'This name already exist in DB'
        """
        query = Department.query.filter(Department.name.like(f'%{name}%')).all()
        if name.lower() in [department.name.lower() for department in query]:
            raise ValidationError('This name already exist in DB')

    @validates_schema(pass_original=True)   
    def is_name_exist(self, data, original_data, **kwargs):
        """Custom field validator for name
        check is id already exist in db, 
        if for current department name change 
        register only or not change at all return None

        :param name: department name
        :type name: str
        :raises ValidationError: This name already exist in DB
        :return: None if same name for current department
        """
        name = data.get('name')
        # if id := data.pop('id', False):
        #     current_employee = Department.query.filter_by(id=id).first()
        #     if name.lower() == current_employee.name.lower():
        #         return
        query = Department.query.filter(Department.name.like(f'%{name}%')).all()
        if name.lower() in [department.name.lower() for department in query]:
            raise ValidationError('This name already exist in DB')


    @validates("id")
    def is_id_exist(self, id: int):
        """Custom field validator for name
        check is name already exist in db

        :param id: department id 
        :type id: int
        :raises ValidationError: 'There is not id in DB'
        """
        if not Department.query.filter_by(id=id).all():
            raise ValidationError('There is not id in DB')

    @post_load
    def make_department(self, data: dict, **kwargs) -> Department:
        """Deserialiaze method for transforming js to ORM object

        :param data: dict with validated parameters
        :type data: dict
        :return: Department object
        :rtype: Department
        """
        return Department(**data)
