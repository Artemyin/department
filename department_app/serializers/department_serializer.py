from marshmallow import fields, validates, ValidationError, post_load

from .serializer import ma
from .employee_serializer import EmployeeSchema

from department_app.models.department_model import Department


class DepartmentSchema(ma.Schema):
    """[summary]

    :param ma: [description]
    :type ma: [type]
    :raises ValidationError: [description]
    :raises ValidationError: [description]
    :return: [description]
    :rtype: [type]
    """
    class Meta:
        model = Department

    id = fields.Integer()
    name = fields.String()
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)
    average_salary = fields.Float(dump_only=True)

    @validates("name")
    def is_name_exist(self, name):
        """[summary]

        :param name: [description]
        :type name: [type]
        :raises ValidationError: [description]
        """
        query = Department.query.filter(Department.name.like(f'%{name}%')).all()
        if name.lower() in [department.name.lower() for department in query]:
            raise ValidationError("This name already exist in DB")

    @validates("id")
    def is_id_exist(self, id):
        """[summary]

        :param id: [description]
        :type id: [type]
        :raises ValidationError: [description]
        """
        if not Department.query.filter_by(id=id).all():
            raise ValidationError("There is not id in DB")

    @post_load
    def make_department(self, data, **kwargs):
        """[summary]

        :param data: [description]
        :type data: [type]
        :return: [description]
        :rtype: [type]
        """
        return Department(**data)
