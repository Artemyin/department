from flask import Blueprint, jsonify, render_template, redirect, request
from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema

from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema

department_service = DepartmentService() 
department_schema = DepartmentSchema(many=True)

employee_service = EmployeeService() 
employee_schema = EmployeeSchema(many=True)


# Blueprint Configuration
department_bp = Blueprint(
    'department_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@department_bp.route('/departments/', methods=['GET'])
def departments():

    departments = department_service.get_all()

    return render_template('departments.html', departments=departments)


@department_bp.route('/departments/<int:id>', methods=['GET'])
def department(id):

    department = department_service.get_by_param(id=id)[0]
    employees = employee_service.get_by_param(department_id=id)
    return render_template('department.html', department=department, employees=employees)
    

@department_bp.route('/departments/', methods=['POST'])
def create_department():
    name = request.form.get("name")
    department_service.add(name=name)
    return redirect('/departments/')

@department_bp.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    department_service.delete(id=id)
    return redirect('/departments/')