from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .department_model import Department
from .employee_model import Employee
