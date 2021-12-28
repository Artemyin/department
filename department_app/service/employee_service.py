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
        try:
            employee = Employee.query.get_or_404(kwargs.pop('id'))
        except Exception:
            raise LookupError
        else:    
            for key, value in kwargs.items():
                setattr(employee, key, value)
            db.session.commit()
            return employee

    def create(self, **kwargs):
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        kwargs['salary'] = int(kwargs.get('salary'))

        # if kwargs.get('department'):
        #     kwargs['department'] = department_service.get_by_param(id=kwargs.get('department'))[0]
        # else: 
        #     kwargs['department'] = None
        if kwargs.get('endpoint', False):
            kwargs.pop('endpoint')
        print(f'service args: {kwargs}')
        
        db.session.add(Employee(**kwargs))
        db.session.commit()
        print("employyee added")
        return self.read_by_param(**kwargs)

    def delete(self, id):
        """[summary]

        :param id: [description]
        :type id: [type]
        :raises LookupError: [description]
        :return: [description]
        :rtype: [type]
        """
        try:
            employee = Employee.query.get_or_404(id)
        except Exception:
            raise LookupError
        else:
            db.session.delete(employee)
            db.session.commit()
            return True

