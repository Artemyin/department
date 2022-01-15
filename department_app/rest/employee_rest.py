from marshmallow import ValidationError
from xmlrpc.client import boolean
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
parser.add_argument('department', required=False, type=int, default=None)


class EmployeeListAPI(Resource):

    @staticmethod
    def get():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        print("call this method")
        #employees = employee_service.read_all()
        #return {'data': employee_schema.dump(employees, many=True)}, 200
        query = Employee.query

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

    @staticmethod
    def post():
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        args = parser.parse_args()

        #errors = employee_schema.validate(args, partial=("department"))
        #print("errors:", errors)
        #print("errors", errors.valid_data)
        #if errors:
        #    return errors, 400
        """
        arguments = (
            name=args['name'],
            birthdate=args['birthdate'],
            salary=args['salary'],
            department=args['department']
        )
        """
        print(f'arguments: {args=}')    
             
        try:
            employee = employee_schema.load(args)
            db.session.add(employee)
            db.session.commit()
        except ValidationError as err:
            print(err.messages)
            return err.messages

        print(f'instance: {employee=}')
        emp = employee_schema.dump(employee)
        print('response', emp)
        return emp, 200


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
        print(f'updated {employee=}')
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
