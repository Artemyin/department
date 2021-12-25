#from sqlalchemy.orm import backref
from datetime import date, datetime

from department_app.models.department_model import Department
from .base import db

class Employee(db.Model):
    """Employee model.

    """
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref="employee")

    
    def __init__(self, name: str, birthdate: date, salary: int, department: Department = None) -> None:
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
        self.department = department
        
            
    def __repr__(self) -> str:

        return f'{self.name}'