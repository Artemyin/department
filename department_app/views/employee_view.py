from marshmallow import ValidationError
from flask import Blueprint, render_template

from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService

from department_app.serializers.employee_serializer import EmployeeSchema
from department_app.serializers.department_serializer import DepartmentSchema


employee_service = EmployeeService() 
department_service = DepartmentService()

employee_schema = EmployeeSchema()
department_schema = DepartmentSchema(many=True)

employee_bp = Blueprint(
    'employee_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@employee_bp.route('/employees/', methods=['GET'])
def employees():
    """This view function handle GET request for 
    render page with list of all employees
    """
    employees = employee_service.read_all()
    departments = department_service.read_all()
    return render_template('employee/employees.html', employees=employees, departments=departments)


@employee_bp.route('/employees/<id>', methods=['GET'])
def employee(id: int):
    """This view function handle GET request for certain id
    render employee page with current id if avalible
    """
    try:
        employee_schema.is_id_exist(id)
        employee = employee_service.read_by_param(id=id)[0]
        departments = department_service.read_all()
    except ValidationError as err:
        return render_template('404.html')
    else:
        return render_template('employee/employee.html', employee=employee, departments=departments)
    
