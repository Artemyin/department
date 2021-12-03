import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from marshmallow_sqlalchemy.fields import Nested

app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig") #Config Production
app.config.from_object(env_config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=False, nullable=False)
    birthdate = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref="employee")

    
    def __init__(self, name, birthdate, salary, departments, *args, **kwargs):
        self.name = name
        self.birthdate = birthdate
        self.salary = salary
        self.department = departments
    
        
    def __repr__(self):
        return f'{self.name}'


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    #employee = db.relationship('Employee', back_populates="department")
     
    def __repr__(self):
        return f'{self.name}'
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    

class EmployeeSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    birthdate = fields.String()
    salary = fields.Integer()
    department = fields.Nested(lambda: DepartmentSchema(only=("id", "name")))

class DepartmentSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    employee = fields.Nested(EmployeeSchema(exclude=("department",)), many=True)
    #employees = fields.List(fields.Nested(EmployeeSchema(exclude=("department",))))
    
            
    #https://marshmallow.readthedocs.io/en/stable/nesting.html
    #https://readthedocs.org/projects/marshmallow-sqlalchemy/downloads/pdf/dev/


@app.route('/')
def index():
    #dep = Department("Engineering")
    
    #db.session.add(dep)
    #emp = Employee("Artemii", "10/10/2000", 120, dep) 
    #db.session.add(emp) 
    #db.session.commit()

    emps = db.session.query(Employee).all()
    deps = db.session.query(Department).all()
    print("----employees----")
    print(emps)
    print("----deparments----")
    print(deps)
    employee_schema = EmployeeSchema(many=True)
    department_schema = DepartmentSchema(many=True)

    jsne = employee_schema.dump(emps)
    jsnd = department_schema.dump(deps)
    print("----serialized--employees----")
    print(jsne)
    print("----serialized--deparments----")
    print(jsnd)
    config = app.config.get("NAME")
    #print(tuple((employee_schema.dump(dep) for dep in deps)))
    return jsonify({"departments":jsnd, "employees":jsne})