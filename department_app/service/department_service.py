from department_app.models.base import db
from department_app.models.department_model import Department
from department_app.service.employee_service import EmployeeService


employee_service = EmployeeService()


class DepartmentService:
    """CRUD service for department model

    implement service database layer, via
    create, read, update, delete methods. 
    """

    def read_all(self) -> list[Department]:
        """Get all Departments from DB
        and return in list.
        """
        departments = Department.query.all()
        return departments


    def read_by_param(self, **kwargs) -> list[Department]:
        """Return filtred list by parameters list of Departments
        """
        departments = Department.query.filter_by(**kwargs).all()
        return departments
         

    def create(self, **kwargs) -> Department:
        """Create new department from passed Department object. 
        """
        department=kwargs.get('department')
        db.session.add(department)
        db.session.commit()
        return department


    def delete(self, id: int) -> None:
        """Delete department from db by department id
        """
        department = Department.query.get(id)
        db.session.delete(department)
        db.session.commit()


    def update(self, **kwargs) -> Department:
        """Update desired department by passing new department object. 
        Update column y column form new to old
        """
        department = Department.query.get_or_404(kwargs.pop('id'))
        args = kwargs.get('department')
        columns = [m.key for m in args.__table__.columns if m.key != 'id']
        for attr in columns:
            setattr(department, attr, args.__getattribute__(attr))
        db.session.commit()
        return department


    def delete_orphans(self, id: int) -> None:
        """Delete employees of certain department
        """
        department = self.read_by_param(id=id)[0]
        for employee in department.employee:
            employee_service.delete(id=employee.id)
        db.session.commit()