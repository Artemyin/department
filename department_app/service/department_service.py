
from department_app.models.department_model import Department
from department_app.models.base import db



class DepartmentService:

    def get_all(self):
        departments = Department.query.all()
        return departments

    def get_by_param(self, **kwargs):
        parameters = ("id", "name")
        
        if not set(kwargs.keys()).issubset(parameters):
            print("model doesn't have this fields, only id or name")
            return False

        departments = Department.query.filter_by(**kwargs).all()
        return departments 

    def add(self, **kwargs):
        
        if self.get_by_param(**kwargs):
            print("This name exist")
            return False 
        db.session.add(Department(**kwargs))
        db.session.commit()
        return self.get_by_param(**kwargs)

    def delete(self, **kwargs):
        instance = self.get_by_param(**kwargs)[0]
        if instance:
            print(f'try to delete {instance=}')
            db.session.delete(instance)
            db.session.commit()
            print("Susesfull deleted")
            return True
        print("no element with his params")
        return False

    def put(self, **kwargs):
        pass

    def path(self, **kwargs):
        pass


