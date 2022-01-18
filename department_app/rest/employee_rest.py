from marshmallow import ValidationError
from flask_restful import Resource, Api, reqparse
from flask import Blueprint, request

from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema


employee_service = EmployeeService()
employee_schema = EmployeeSchema()

api_employee_bp = Blueprint('employee_api', __name__)
api = Api(api_employee_bp)

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='Name cannot be blank!')
parser.add_argument('birthdate', required=True, help='Birthdate cannot be blank!')
parser.add_argument('salary', required=True, type=int, help='Salary cannot be blank!')
parser.add_argument('department', required=True, type=int, default=None)


class EmployeeListAPI(Resource):

    @staticmethod
    def get():
        """[summary]

        :return: [description]
        :rtype: [type]
        """

        args = request.args
        employees = employee_service.search(args)
        return {
            'data': employee_schema.dump(employees.query, many=True),
            'recordsFiltered': employees.total_filtered,
            'recordsTotal': employees.recordstotal,
            'draw': employees.draw, 
        }
    
    @staticmethod
    def post():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        args = parser.parse_args()
        try:
            employee = employee_schema.load(args)
            employee = employee_service.create(employee=employee)
        except ValidationError as err:
            return err.messages
        else:
            return employee_schema.dump(employee), 200


class EmployeeAPI(Resource):

    @staticmethod
    def get(id: int):
        """[summary]

        :param id: [description]
        :type id: int
        :return: [description]
        :rtype: [type]
        """
        try:
            employee_schema.is_id_exist(id)
            employee = employee_service.read_by_param(id=id)[0]
        except ValidationError as err:
            return err.messages, 404
        else:
            return employee_schema.dump(employee), 200
        

    @staticmethod
    def put(id: int):
        """[summary]

        :param id: [description]
        :type id: int
        :return: [description]
        :rtype: [type]
        """
        args = parser.parse_args()
        try:
            employee_schema.is_id_exist(id)
            employee = employee_schema.load(args)
            employee = employee_service.update(employee=employee, id=id)   
        except ValidationError as err:
            return err.messages, 400
        else:
            return employee_schema.dump(employee), 200

    @staticmethod
    def delete(id: int):
        """Handle DELETE request for department/<id>
        if department with this id exist it will be deleted
        and return HTTP status code 204

        :param id: desired department to delete
        :type id: int
        :return: 204 HTTP status code if sucesfull
        :rtype: HTTP status code
        """
        try:
            employee_schema.is_id_exist(id)
            employee_service.delete(id)
        except ValidationError as err:
            return err.messages, 404
        else:
            return 204



api.add_resource(EmployeeListAPI, '/employees/')
api.add_resource(EmployeeAPI, '/employees/<int:id>')
