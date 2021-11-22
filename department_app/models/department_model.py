from .base import db
from .employee_model import Employee

class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    employee = db.relationship('Employee', back_populates="department")
     
    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name):
        super().__init__()
        self.name = name
