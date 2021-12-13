from department_app.models import db
from department_app.models.employee_model import Employee
from department_app.service.department_service import DepartmentService


department_service = DepartmentService()


class EmployeeService:

    def get_all(self):
        employees = Employee.query.all()
        return employees

    def get_by_param(self, **kwargs):
        employees = Employee.query.filter_by(**kwargs).all()
        return employees 
        

    def put(self, **kwargs):
        
        try:
            employee = Employee.query.get_or_404(kwargs.pop('id'))
        except Exception:
            raise LookupError
        else:    
            for key, value in kwargs.items():
                setattr(employee, key, value)
            db.session.commit()
            return employee

    def add(self, **kwargs):
        kwargs['salary'] = int(kwargs.get('salary'))

        # if kwargs.get('department'):
        #     kwargs['department'] = department_service.get_by_param(id=kwargs.get('department'))[0]
        # else: 
        #     kwargs['department'] = None
        if kwargs.get('endpoint', False):
            kwargs.pop('endpoint')
        print(kwargs)
        
        db.session.add(Employee(**kwargs))
        db.session.commit()
        print("employyee added")
        return self.get_by_param(**kwargs)

    def delete(self, id):
        try:
            employee = Employee.query.get_or_404(id)
        except Exception:
            raise LookupError
        else:
            db.session.delete(employee)
            db.session.commit()
            return True

