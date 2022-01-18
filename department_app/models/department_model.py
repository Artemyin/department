from .base import db
#from .employee_model import Employee

class Department(db.Model):
    """[summary]

    :param db: [description]
    :type db: [type]
    :return: [description]
    :rtype: [type]
    """
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    employee = db.relationship('Employee', back_populates="department")
    
    @property
    def average_salary(self):
        try:
            return round(sum(employee.salary for employee in self.employee)/len(self.employee), 2)
        except ZeroDivisionError:
            return 0

    def __repr__(self) -> str:
        """[summary]

        :return: [description]
        :rtype: str
        """
        return f'{self.name}'
    
    def __init__(self, name: str):
        """[summary]

        :param name: [description]
        :type name: str
        """
        self.name = name
    