#from department_app.models import db
#from department_app.models.department_model import Department
#from department_app.models.employee_model import Employee 


#print("------try to delete db-----")
"""
print(Department.query.all())
if Department.query.all():
    db.session.query(Department).delete()

print(Employee.query.all())    
if Employee.query.all():
    db.session.query(Employee).delete()

db.session.commit()"""
#print("------beign filling db-----")
departments = ["Management", "Sales", "Engineering", "Service", None, "Engineering"]

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
    
]


#for department in departments:
    #print(department)
    #dep = Department(department)
    #emps_dep.append(dep)
    #db.session.add(dep)

#emps_dep.append(None)
#dep = Department(departments[2])
#emps_dep.append(dep)

ziped_emps = list(zip(emps_names, emps_birthdays, emps_salary, emps_dep))


#for i in range(6):
    #db.session.add(Employee(emps_names[i], emps_birthdays[i], emps_salary[i], emps_dep[i]))

#db.session.commit()



