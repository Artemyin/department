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
        department=kwargs.get('department')
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
        department = Department.query.get(id)
        db.session.delete(department)
        db.session.commit()


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
        department = Department.query.get_or_404(kwargs.pop('id'))
        args = kwargs.get('department')
        columns = [m.key for m in args.__table__.columns if m.key != 'id']
        for attr in columns:
            setattr(department, attr, args.__getattribute__(attr))
        db.session.commit()
        return department

