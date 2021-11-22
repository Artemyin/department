from department_app.models.department_model import Department
from department_app.models import db

class DepartmentService:

    def get_all():
        departments = Department.query.all()
        return departments
        pass

    def get_by_param(*kwargs):
        pass

    def add(*kwargs):
        pass

    def delete(*kwargs):
        pass

    def put(*kwargs):
        pass

    def path(*kwargs):
        pass


