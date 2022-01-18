from datetime import datetime
from collections import namedtuple

from department_app.models import db
from department_app.models.employee_model import Employee



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

    def search(self, args):
        department_id=args.get('department_id')
        start_date = args.get('start_date')
        end_date = args.get('end_date')
        search = args.get('search[value]')
        start = args.get('start', type=int)
        length = args.get('length', type=int)
        draw = args.get('draw', type=int)
        get_col_index = lambda i: args.get(f'order[{i}][column]')
        get_col_name = lambda col_index: args.get(f'columns[{col_index}][data]')
        get_descending = lambda i: args.get(f'order[{i}][dir]')

        query = Employee.query
        if department_id: # If department specified filter all employee in this dep
            query = query.filter_by(department_id=department_id)
        query = self.datarange_filter(query, start_date, end_date)
        query, total_filtered = self.search_filter(query, search)
        query = self.sort_data(query, get_col_index, get_col_name, get_descending)
        query = self.paginate_data(query, start, length)
        recordstotal = Employee.query.count()

        result = namedtuple("result", ["query", "total_filtered", "recordstotal", "draw"])
        return result(
            query,
            total_filtered, 
            recordstotal, 
            draw
        )

    def datarange_filter(self, query, start_date, end_date):
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            start_date = datetime(1900, 1, 1) 
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end_date = datetime.now()
        query = query.filter(Employee.birthdate.between(start_date,end_date))
        return query

    def search_filter(self, query, search):
        if search:
            query = query.filter(Employee.name.like(f'%{search}%'))
        total_filtered = query.count()
        return query, total_filtered

       
    def sort_data(self, query, get_col_index, get_col_name, get_descending):
        order = []
        i = 0
        while True:
            col_index = get_col_index(i)
            if col_index is None:
                break
            col_name = get_col_name(col_index)
            if col_name not in ['id',  'name', 'birthdate', 'salary',]:
                col_name = 'name'
            descending = get_descending(i) == 'desc'
            col = getattr(Employee, col_name)
            if descending:
              col = col.desc()
            order.append(col)
            i += 1
        if order:
            query = query.order_by(*order)
        return query

    
    def paginate_data(self, query, start, length):
        query = query.offset(start).limit(length)
        return query

