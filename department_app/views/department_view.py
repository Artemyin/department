from flask import Blueprint, jsonify, render_template, redirect, request
from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema

from department_app.service.employee_service import EmployeeService
from department_app.serializers.employee_serializer import EmployeeSchema

department_service = DepartmentService() 
department_schema = DepartmentSchema(many=True)


# Blueprint Configuration
department_bp = Blueprint(
    'department_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@department_bp.route('/departments/', methods=['GET'])
def departments():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    departments = department_service.get_all()
    return render_template('department/departments.html', departments=departments)


@department_bp.route('/departments/<int:id>', methods=['GET'])
def department(id: int):
    """[summary]

    :param id: [description]
    :type id: [type]
    :return: render HTML page with 
    :rtype: HTML
    """
    department = department_service.get_by_param(id=id)[0]
    departments = department_service.get_all()
    return render_template('department/department.html', departments=departments, department=department)
    

@department_bp.route('/departments/', methods=['POST'])
def create_department():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    data = request.form
    department_service.add(**data)
    return redirect('/departments/')


@department_bp.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id: int):
    """[summary]

    :param id: [description]
    :type id: [type]
    :return: [description]
    :rtype: [type]
    """
    department_service.delete(id)
    return redirect('/departments/'), 204
    

@department_bp.route('/departments/<int:id>', methods=['PUT'])
def edit_department(id: int):
    """[summary]

    :param id: [description]
    :type id: [type]
    :return: [description]
    :rtype: [type]
    """
    print("put is working")
    data = request.get_json()
    department_service.put(id=id, name=data.get('name'))
    
    return departments(), 204