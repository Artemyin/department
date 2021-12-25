from flask import Blueprint, jsonify, render_template, redirect, request

from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService

from department_app.serializers.employee_serializer import EmployeeSchema
from department_app.serializers.department_serializer import DepartmentSchema


employee_service = EmployeeService() 
department_service = DepartmentService()


employee_schema = EmployeeSchema(many=True)
department_schema = DepartmentSchema(many=True)

# Blueprint Configuration
employee_bp = Blueprint(
    'employee_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@employee_bp.route('/employees/', methods=['GET'])
def employees():
    employees = employee_service.read_all()
    departments = department_service.read_all()
    return render_template('employee/employees.html', employees=employees, departments=departments)


@employee_bp.route('/employees/<int:id>', methods=['GET'])
def employee(id: int):
    employee = employee_service.read_by_param(id=id)[0]
    return render_template('employee/employee.html', employee=employee)
    

@employee_bp.route('/employees/', methods=['POST'])
def create_employee():
    data = request.form
    endpoint = data.get('endpoint')
    employee_service.create(**data)
    return redirect(endpoint)


@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    employee_service.delete(id=id)
    return redirect('/employees/'), 204
    

@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def edit_employee(id: int):
    data = request.json()
    employee_service.update(id=id, data=data)
    return redirect('/employees/'), 204