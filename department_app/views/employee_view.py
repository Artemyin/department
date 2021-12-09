from os import name
from flask import Blueprint, jsonify, render_template

from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema

from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema

emp_service = EmployeeService() 
emp_schema = EmployeeSchema(many=True)



# Blueprint Configuration
employee_bp = Blueprint(
    'employee_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@employee_bp.route('/employees/', methods=['GET'])
def employee():

    emps= emp_service.get_all()

    return render_template('employee/employees.html', employees=emps)

