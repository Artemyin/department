from datetime import datetime

from department_app.models import db
from department_app.models.employee_model import Employee
from department_app.service.department_service import DepartmentService


department_service = DepartmentService()


class EmployeeService:
    """CRUD service for employee model

    implement service database layer, via
    create, read, update, delete methods. 

    :methods: 
        * get_all(),
        * get_by_param(**kwargs),
        * create(**kwargs),
        * update(**kwargs),
        * delete(id)
    """

    def read_all(self) -> list[Employee]:
        """read_all read all Employees from db
        and return in list

        :return: list of all Employees in db
        :rtype: list of instances Employee class
        """
        employees = Employee.query.all()
        return employees

    def read_by_param(self, **kwargs)  -> list[Employee]:
        """[summary]

        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *id* (``int``) --
              employee id
            * *name* (``str``) --
              employee name
            * *birthdate* (``datetime``) --
              employee name
            * *salary* (``int``) --
              employee name              
            * *department* (``Departemnt``) --
              employee name            

        :return: [description]
        :rtype: list[Employee]
        """
        employees = Employee.query.filter_by(**kwargs).all()
        return employees 
        

    def update(self, **kwargs):
        """[summary]

        :raises LookupError: [description]
        :return: [description]
        :rtype: [type]
        """        
        employee = Employee.query.get_or_404(kwargs.pop('id'))
        args = kwargs.get('employee')
        columns = [m.key for m in args.__table__.columns if m.key != 'id']
        for attr in columns:
            setattr(employee, attr, args.__getattribute__(attr))
        db.session.commit()
        return employee


    def create(self, **kwargs):
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        employee = kwargs.get('employee')
        db.session.add(employee)
        db.session.commit()
        return employee
    

    def delete(self, id):
        """[summary]

        :param id: [description]
        :type id: [type]
        :return: [description]
        :rtype: [type]
        """
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
  

