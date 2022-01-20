from datetime import datetime
from collections import namedtuple

from department_app.models import db
from department_app.models.employee_model import Employee



class EmployeeService:
    """CRUD service for employee model.

    implement service database layer, via
    create, read, update, delete, search methods. 
    """

    def read_all(self) -> list[Employee]:
        """read_all read all Employees from db
        and return in list.
        """
        employees = Employee.query.all()
        return employees

    def read_by_param(self, **kwargs)  -> list[Employee]:
        """Return filtred list by parameters list of Employees.
        """
        employees = Employee.query.filter_by(**kwargs).all()
        return employees 
        
    def update(self, **kwargs):
        """Update desired employee by passing new employee object. 
        Update column by column form new to old.
        """       
        employee = Employee.query.get_or_404(kwargs.pop('id'))
        args = kwargs.get('employee')
        columns = [m.key for m in args.__table__.columns if m.key != 'id']
        for attr in columns:
            setattr(employee, attr, args.__getattribute__(attr))
        db.session.commit()
        return employee

    def create(self, **kwargs):
        """Create new employee from passed Employee object. 
        """
        employee = kwargs.get('employee')
        db.session.add(employee)
        db.session.commit()
        return employee

    def delete(self, id):
        """Delete employee from db by employee id
        """
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()

    def search(self, args):
        """Filter query by passed arguments,
        filter all employees for certain departments,
        filter by datarange, search employees name,
        sorting data, paginate data.

        :return: namedtuple for stright access to returned data
        :rtype: namedtuple
        """
        
        draw = args.get('draw', type=int)
        
        query = Employee.query
        query = self.department_filter(query, args)
        query = self.datarange_filter(query, args)
        query, total_filtered = self.search_filter(query, args)
        query = self.sort_data(query, args)
        query = self.paginate_data(query, args)
        recordstotal = Employee.query.count()

        result = namedtuple("result", ["query", "total_filtered", "recordstotal", "draw"])
        return result(
            query,
            total_filtered, 
            recordstotal, 
            draw
        )

    def department_filter(self, query, args):
        """Filtering Employyes of certain department.
        """
        department_id = args.get('department_id')
        if department_id: 
           query = query.filter_by(department_id=department_id)
        return query

    def datarange_filter(self, query, args):
        """Filtering Employees from start_date to end_date.
        if start_date not specify, start_date will assign to default- 1900, 1, 1
        if end_date not specify, end_date will assign to default - current time
        """
        start_date = args.get('start_date')
        end_date = args.get('end_date')
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

    def search_filter(self, query, args):
        """Filtering Employees by name 

        :return: employee query, total_filtered employee
        :rtype: query, int
        """
        search = args.get('search[value]')
        if search:
            query = query.filter(Employee.name.like(f'%{search}%'))
        total_filtered = query.count()
        return query, total_filtered
       
    def sort_data(self, query, args):
        """Sorting columns order and asc is passed by arguments
        """
        get_col_index = lambda i: args.get(f'order[{i}][column]')
        get_col_name = lambda col_index: args.get(f'columns[{col_index}][data]')
        get_descending = lambda i: args.get(f'order[{i}][dir]')
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
    
    def paginate_data(self, query, args):
        """Paginate query
        """
        start = args.get('start', type=int)
        length = args.get('length', type=int)
        query = query.offset(start).limit(length)
        return query

