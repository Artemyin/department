from datetime import datetime
from marshmallow import ValidationError

from flask_restful import Resource
from flask import Blueprint, request
from flask_restful import Api, reqparse
from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema




from department_app.models import db


employee_service = EmployeeService()
employee_schema = EmployeeSchema()

api_employee_bp = Blueprint('employee_api', __name__)
api = Api(api_employee_bp)


from department_app.models.employee_model import Employee

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

        """
        print("call this method")
        #employees = employee_service.read_all()
        #return {'data': employee_schema.dump(employees, many=True)}, 200
        query = Employee.query



        # daterange
        start_date_raw = request.args.get('start_date')
        end_date_raw = request.args.get('end_date')

        if start_date_raw:
            start_date = datetime.strptime(start_date_raw, '%Y-%m-%d')
        else:
            start_date = datetime(1900, 1, 1) 

        if end_date_raw:
            end_date = datetime.strptime(end_date_raw, '%Y-%m-%d')
        else:
            end_date = datetime.now()

        query = query.filter(Employee.birthdate.between(start_date,end_date))
       
        # search filter
        search = request.args.get('search[value]')
        if search:
            query = query.filter(Employee.name.like(f'%{search}%'))
        total_filtered = query.count()

        # pagination
        start = request.args.get('start', type=int)
        length = request.args.get('length', type=int)
        query = query.offset(start).limit(length)

        # response
        return {
            'data': employee_schema.dump(query, many=True),
            'recordsFiltered': total_filtered,
            'recordsTotal': Employee.query.count(),
            'draw': request.args.get('draw', type=int), 
        }
        """

        args = request.args
        employees = employee_service.search(args)

        # response
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
        employee = employee_schema.dump(employee)
        return employee, 200


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
        try:
            employee_schema.is_id_exist(id)
            employee = employee_schema.load(args)
            employee = employee_service.update(employee=employee, id=id)   
        except ValidationError as err:
            return err.messages
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
            return err.messages, 400
        else:
            return 204

def data_parse_args(arg):
    start = arg.get('start', type=int)
    return start

api.add_resource(EmployeeListAPI, '/employees/')
api.add_resource(EmployeeAPI, '/employees/<int:id>')
