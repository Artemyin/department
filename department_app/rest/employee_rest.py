from flask_restful import Resource
from flask import Blueprint
from flask_restful import Api, reqparse
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
parser.add_argument('department', required=False)


class EmployeeListAPI(Resource):

    @staticmethod
    def get():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        employees = employee_service.read_all()
        return employee_schema.dump(employees, many=True), 200
    

    @staticmethod
    def post():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        args = parser.parse_args()
        employee = employee_service.create(
            name=args['name'],
            birthdate=args['birthdate'],
            salary=args['salary'],
            department=args['department']
        )
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
        employee = employee_service.read_by_param(id=id)[0]
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
        employee = employee_service.update(
            id=id,
            name=args['name'],
            birthdate=args['birthdate'],
            salary=args['salary'],
            department=args['department']
        )
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
            employee_service.delete(id)
        except:
            return 400
        else:
            return 204


api.add_resource(EmployeeListAPI, '/employees/')
api.add_resource(EmployeeAPI, '/employees/<int:id>')
