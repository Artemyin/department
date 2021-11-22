from . import db

class Employee(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=False, nullable=False)
    birthdate = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', back_populates="employee")

    def __init__(self, name, birthdate, salary, department_id=None):
        self.name = name
        self.birthdate = birthdate
        self.salary = salary
        self.department_id = department_id
    
    def __repr__(self):
        return f'{self.name}'