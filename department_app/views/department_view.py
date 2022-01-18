from flask import Blueprint, render_template
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
    