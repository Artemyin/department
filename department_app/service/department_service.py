from department_app.models.base import db
from department_app.models.department_model import Department


class DepartmentService:

    def get_all(self):
        departments = Department.query.all()
        return departments

    def get_by_param(self, **kwargs):
        departments = Department.query.filter_by(**kwargs).all()
        if departments:
            return departments
         

    def add(self, **kwargs):

        if self.get_by_param(name=kwargs.get('name')):
            print("This name exist")
            return False 
        department = Department(**kwargs)
        db.session.add(department)
        db.session.commit()
        return department

    def delete(self, id):
        try:
            department = Department.query.get_or_404(id)
        except Exception:
            raise LookupError
        else:
            db.session.delete(department)
            db.session.commit()
            return True

    def put(self, **kwargs):

        try:
            department = Department.query.get_or_404(kwargs.pop('id'))
        except Exception:
            raise LookupError
        else:    
            for key, value in kwargs.items():
                setattr(department, key, value)
            db.session.commit()
            return department