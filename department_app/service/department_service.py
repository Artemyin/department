from department_app.models.base import db
from department_app.models.department_model import Department
from department_app.service.employee_service import EmployeeService


employee_service = EmployeeService()


class DepartmentService:
    """CRUD service for department model

    implement service database layer, via
    create, read, update, delete methods. 

    :methods: 
        * get_all(),
        * get_by_param(**kwargs),
        * create(**kwargs),
        * update(**kwargs),
        * delete(id),
    """

    def read_all(self) -> list[Department]:
        """Get all Departments from DB
        and return in list.

        :return: all departments
        :rtype: list[Department]
        """
        departments = Department.query.all()
        return departments


    def read_by_param(self, **kwargs) -> list[Department]:
        """Return filtred list of Departments

        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *id* (``int``) --
              department id
            * *name* (``str``) --
              department name


        :return: filtred departments
        :rtype: list[Department]
        """
        departments = Department.query.filter_by(**kwargs).all()
        return departments
         

    def create(self, **kwargs) -> Department:
        """Create new department from
        passed Department object. 
 
        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *department* (``Department``) --
              department object

        :return: created Department 
        :rtype: Department 
        """
        department=kwargs.get('department')
        db.session.add(department)
        db.session.commit()
        return department


    def delete(self, id: int) -> None:
        """Delete department from db
        by department id

        :param id: department to delete from db
        :type id: int
        :return: None
        :rtype: None
        """
        department = Department.query.get(id)
        db.session.delete(department)
        db.session.commit()


    def update(self, **kwargs) -> Department:
        """Update desired department
        by passing new department object. 
        Update column y column form new to old
        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *id* (``int``) --
              department id
            * *department* (``Department``) --
              department object
           
        :return: updated department 
        :rtype: Department object
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

        :param id: department id
        :type id: int
        """
        department = self.read_by_param(id=id)[0]
        for employee in department.employee:
            employee_service.delete(id=employee.id)
        db.session.commit()