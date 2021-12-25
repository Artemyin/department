from flask import Blueprint, jsonify, render_template, redirect, request
from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema

from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema

department_service = DepartmentService() 



# Blueprint Configuration
department_bp = Blueprint(
    'department_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@department_bp.route('/departments/', methods=['GET'])
def departments():
    """This view function handle GET request for 
    render page with list of all departments

    :return: render HTML template with list of all departments
    :rtype: HTML
    """
    departments = department_service.read_all()
    return render_template('department/departments.html', departments=departments)


@department_bp.route('/departments/<int:id>', methods=['GET'])
def department(id: int):
    """This view function handle GET request for certain id
    render departemnt page with current id if avalible

    :param id: id of department to render
    :type id: int
    :return: render HTML page with desired department
            and departments for select html element
    :rtype: render_template()
    """
    department = department_service.read_by_param(id=id)[0]
    departments = department_service.read_all()
    return render_template('department/department.html', departments=departments, department=department)
    

@department_bp.route('/departments/', methods=['POST'])
def create_department():
    """This view function handle POST request
    for creating new department. Get data from json, not form.

    :return: redirect to /departments/ page
    :rtype: redirect() to HTML
    """
    data = request.get_json()
    department_service.create(name=data.get('name'))
    return redirect('/departments/')


@department_bp.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id: int):
    """This view function handle DELETE request
    for deleting department by id. 

    :param id: desired department to delete
    :type id: int
    :return: redirect to /department/, and HTTP status code 204 if succesful
    :rtype: redirect(), HTTP status code
    """
    department_service.delete(id)
    return redirect('/departments/'), 204
    

@department_bp.route('/departments/<int:id>', methods=['PUT'])
def edit_department(id: int):
    """This view function handle PUT request
    for update department by id. data gets via
    request in json format.
    This view doesn't render any page, but call 
    departments view function   

    :param id: id department to update
    :type id: int
    :return: call department view function, and HTTP status code 204 if succesful
    :rtype: department view functionm, HTTP status code
    """
    data = request.get_json()
    department_service.update(id=id, name=data.get('name'))
    return departments(), 204