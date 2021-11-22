from department_app import db
from department_app.models import Employee, Department


db.session.query(Employee).delete()
db.session.query(Department).delete()
db.session.commit()

departments = ["Management", "Sales", "Department", "Service"]

emps_names = [
    'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie'
]

emps_birthdays = [
    "01/10/2000", "02/10/2000", "03/10/2000", "04/10/2000", "05/10/2000", "06/10/2000"
]

emps_salary = [
    110, 120, 130, 140, 150, 160
]

emps_dep = [
    1, 2, 3, 4, None, 1
]

ziped_emps = list(zip(emps_names, emps_birthdays, emps_salary, emps_dep))

for departament in departments:
    db.session.add(Department(departament))

for emp in ziped_emps:
    db.session.add(Employee(*emp))

db.session.commit()



