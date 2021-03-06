from datetime import date

from .base import db


class Employee(db.Model):
    """Employee orm model
    """
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=True)
    department = db.relationship('Department', back_populates="employee")

    
    def __init__(self, name: str, birthdate: date, salary: int, department=None) -> None:
        """Employee model constructor.

        :param name: employee name
        :type name: str
        :param birthdate: employee birthdate
        :type birthdate: date
        :param salary: employee salary
        :type salary: int
        :param department: employee department, defaults to None
        :type department: Department, optional
        """
        self.name = name
        self.birthdate = birthdate
        self.salary = salary
        self.department_id = department
        
            
    def __repr__(self) -> str:
        """Representation info about department.
        """
        return f'{self.name}'