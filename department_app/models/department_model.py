from .base import db


class Department(db.Model):
    """Department orm model

    :columns: 
        * id: primary key,
        * name: string,
        * employees: list[Employee] relationship with Employee table,
    """
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    employee = db.relationship('Employee', back_populates="department")
    
    @property
    def average_salary(self) -> float:
        """Departmen's employees average salary property

        :return: department's demployees average salary 
        :rtype: float
        """
        try:
            return round(sum(employee.salary for employee in self.employee)/(1 or len(self.employee)), 2)
        except ZeroDivisionError:
            return 0

    def __repr__(self) -> str:
        """beautiful representation info 
        about department.

        :return: name of department
        :rtype: str
        """
        return f'{self.name}'
    
    def __init__(self, name: str):
        """Department model constructor.

        :param name: Department's name
        :type name: str
        """
        self.name = name
    