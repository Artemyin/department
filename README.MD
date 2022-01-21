Structure of project

department-app (a project / app directory)

- migrations (this package include migration files to manage database schema changes )

- models (this package include modules with Python classes describing DB models (for ORM only))

- service (this package include modules with functions / classes to work with DB (CRUD operations))

- serializers (this package include modules with functions / classes to serialize, deserialize and validation data

- rest (this package include modules with RESTful service implementation)

- templates (this folder include web app html templates)

- static (this folder must static files (js, css, images, etc,))

- views (this package must modules with Web controllers / views) 

#### Technologies:
- Python 3.9
- from flask_sqlalchemy - SQLAlchemy
- from flask-Mrshmallow - Mrshmallow
- from flask-migrate - Migrate
- flask_restful
- JavaScript
- DataTables.js 


Setup
1. Clone repo
2. Create virtual environment
3. Install project requirements
5. Run the migration scripts to create database schema
5. [optional] Run populate fake db comant to create fake data

python populate_fake_table.py

6. [optional] Run wipe fake data for erasing data base

python wipe_data.py

7. run application

  - flask run:

  - http://127.0.0.1:5000/ 

  - flask run --host=0.0.0.0:

  - http://192.168.1.155:5000/ 

#### Departments api:
 - GET /api/v1/departments - return all departments in json format
 
 - POST /api/v1/departments - add a new department to the database (post request must be followed
 with json with the fields to add). Example:  
 ```json
[
  {
    "employees": [
      {
        "date_of_birth": "07/12/1999", 
        "hospital_id": "Paramedical", 
        "id": 56, 
        "name": "John Doe", 
        "salary": 1300
      }
    ], 
    "id": 97, 
    "name": "Paramedical", 
    "to_do": "something do1"
  }
]
```
- GET /api/v1/departments/*id* - return the department with the given id 
in json format
- PUT /api/v1/departments/*id* - updates the department with the given id
with the values, provided in json format. Example:  
 ```json
{
  "employees": [
    {
      "date_of_birth": "11/30/1989", 
      "hospital_id": "Nurcing department", 
      "id": 58, 
      "name": "Will Hunting", 
      "salary": 1300
    }
  ], 
  "id": 99, 
  "name": "Nurcing department", 
  "to_do": "something do2"
}
```
- DELETE /api/v1/departments/*id*?orphan=0 - deletes the department with the given id, employee of this department will move to None department

- DELETE /api/v1/departments/*id*?orphan=1 - deletes the department with his employees by the given id 

   
   #### Employees api
 - GET /api/v1/employees - return all employees in json format
 - POST /api/v1/employees - add a new employee to the database (post request must be followed
 with json with the fields to add). Example:  
 ```json
  {
    "date_of_birth": "07/12/1999", 
    "hospital": "Paramedical", 
    "id": 56, 
    "name": "John Doe", 
    "salary": 1300
  }
```

- GET /api/v1/employees/*id* - return the employee with the given id 
in json format
- PUT /api/v1/employees/*id* - updates the employee with the given id
with the values, provided in json format. Example:  
 ```json
 {
  "date_of_birth": "07/12/1999", 
  "hospital_id": "Paramedical", 
  "id": 56, 
  "name": "John Doe", 
  "salary": 1300
}
```
- DELETE /api/v1/employees/*id* - deletes the employee with the given id  
- GET /api/v1/employees?date=*date*'- searches employees born on a specific date (replace the *date* with some value)
and returns them in json format
  
 ```json
  {
    "date_of_birth": "01/08/1993", 
    "hospital_id": "Phisical medicine", 
    "id": 57, 
    "name": "Jane Wilson", 
    "salary": 1300
  }
```
- GET /api/v1/employees?start_date='*start_date*'&end_date='*end_date*' - 
  search employees born on a specific date range
   (replace the *start_date* and *end_date* with some value) and returns
   them in json format
  

```json
     {
    "date_of_birth": "01/08/1993", 
    "hospital_id": "Phisical medicine", 
    "id": 57, 
    "name": "Jane Wilson", 
    "salary": 1300
  }
```


#### Here is the list of available addresses of web application:

 


 #### Departments

 - /departments - display all the departments
 - /departments/*id* - display certain department by id
   
   
#### Employees

 - /employees - display all the employees
 - /employees/*id* - display certain employee by id
