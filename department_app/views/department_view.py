from marshmallow import ValidationError
from flask import Blueprint, jsonify, render_template, abort

from department_app.service.department_service import DepartmentService
from department_app.serializers.department_serializer import DepartmentSchema


department_service = DepartmentService() 
department_schema = DepartmentSchema()

department_bp = Blueprint(
    'department_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@department_bp.route('/departments/', methods=['GET'])
def departments():
    """This view function handle GET request for 
    render page with list of all departments
    """
    departments = department_service.read_all()
    return render_template('department/departments.html', departments=departments)


@department_bp.route('/departments/<id>', methods=['GET'])
def department(id: int):
    """This view function handle GET request for certain id
    render departemnt page with current id if avalible
    """
    try:
        department_schema.is_id_exist(id)
        department = department_service.read_by_param(id=id)[0]
        departments = department_service.read_all()
    except ValidationError as err:
        return render_template('404.html')
    else:
        return render_template('department/department.html', departments=departments, department=department)

