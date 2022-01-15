from department_app.models.base import db
from department_app.models.department_model import Department



class DepartmentService:

    def read_all(self):
        departments = Department.query.all()
        return departments

    def read_by_param(self, **kwargs):
        departments = Department.query.filter_by(**kwargs).all()
        return departments
            
         

    def create(self, **kwargs) -> Department:
        """Create new department with
        passed parameters. 
        if department with same name exist 
        this method return False

        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *id* (``int``) --
              department id
            * *name* (``str``) --
              department name

        :return: created Department or False if cannot create department with this name
        :rtype: Department | bool
        """
        if self.read_by_param(name=kwargs.get('name')):
            print("This name exist")
            return False 
        department = Department(**kwargs)
        db.session.add(department)
        db.session.commit()
        return department

    def delete(self, id: int) -> bool:
        """Delete department from db
        by id

        :param id: department to delete from db
        :type id: int
        :raises LookupError: raise if department with this id doesn't exist
        :return: True if department deleted succesfull
        :rtype: bool
        """
        try:
            department = Department.query.get_or_404(id)
        except Exception:
            raise LookupError
        else:
            print(f'delete {department}')
            #db.session.delete(department)
            db.session.commit()
            return True

    def update(self, **kwargs) -> Department:
        """[summary]

        :param \**kwargs:
            see below

        :Keyword Arguments:
            * *id* (``int``) --
              department id
            * *name* (``str``) --
              department name
           

        :return: updated department 
        :rtype: Department object
        """
        try:
            department = Department.query.get_or_404(kwargs.pop('id'))
        except Exception:
            raise LookupError
        else:    
            for key, value in kwargs.items(): # Parse kwargs.
                setattr(department, key, value) # Reassign to deppartment new value by key.
            db.session.commit()
            return department # Return updated department.