from marshmallow import ValidationError
from flask_restful import Resource
from flask import Blueprint, request
from flask_restful import Api, reqparse
import requests
from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema

department_service = DepartmentService()
department_schema = DepartmentSchema()

from department_app.service.employee_service import EmployeeService
employee_service = EmployeeService()

api_department_bp = Blueprint('departemnt_api', __name__)
api = Api(api_department_bp)

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='Name cannot be blank!')

class DepartmentListAPI(Resource):

    @staticmethod
    def get():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        departments = department_service.read_all()
        return department_schema.dump(departments, many=True), 200

    @staticmethod
    def post():
        """[summary]
        """
        args = parser.parse_args()
        try:
            department = department_schema.load(args)
            department = employee_service.create(department=department)
        except ValidationError as err:
            return err.messages
        return department_schema.dump(department), 200
        

class DepartmentAPI(Resource):

    @staticmethod
    def get(id: int):
        """Handle GET request for department/<id>
        via id get department and return
        json with http response code
        
        :param id: department id
        :type id: int
        :return: department json and HTTP status code 200 if succesfull
        :rtype: JSON, HTTP status code
        """
        data = {'id': id}
        errors = department_schema.validate(data)
        print("errors", errors)
        if errors:
            return errors, 400
        department = department_service.read_by_param(id=id)[0]
        return department_schema.dump(department), 200
        
    @staticmethod
    def put(id: int):
        """Handle PUT request for department/<id>
        parse arguments from json and update desired department

        :param id: 
        :type id: int
        :return: [description]
        :rtype: [type]
        """
        args = parser.parse_args()
        try:
            department_schema.is_id_exist(id)
            department = department_schema.load(args)
            department = department_service.update(department=department, id=id)   
        except ValidationError as err:
            return err.messages
        return department_schema.dump(department), 200

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
        orphan = request.args.get('orphan', type=int)
        if orphan:
            department = department_service.read_by_param(id=id)[0]
            for employee in department.employee:
                employee_service.delete(id=employee.id)
        try:
            department_schema.is_id_exist(id)
            department_service.delete(id)
        except ValidationError as err:
            return err.messages, 400
        else:
            return 204

api.add_resource(DepartmentListAPI, '/departments/')
api.add_resource(DepartmentAPI, '/departments/<int:id>')