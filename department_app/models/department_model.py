from .base import db


class Department(db.Model):
    """Department orm model
    """
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    employee = db.relationship('Employee', back_populates="department")
    
    @property
    def average_salary(self) -> float:
        """Departmen's employees average salary property
        """
        try:
            return round(sum(employee.salary for employee in self.employee)/(len(self.employee) or 1), 2)
        except ZeroDivisionError:
            return 0
    
    def __init__(self, name: str):
        """Department model constructor.

        :param name: Department's name
        :type name: str
        """
        self.name = name
        
    def __repr__(self) -> str:
        """Representation info about department.
        """
        return f'{self.name}'