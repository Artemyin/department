#### Structure of project

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


#### Setup
1. Clone repo
2. Create virtual environment
3. Install project requirements
5. Run the migration scripts to create database schema
5. [optional] Run populate fake db comant to create fake data

- python populate_fake_table.py

6. [optional] Run wipe fake data for erasing data base

- python wipe_data.py

7. run application

  - flask run:

  - http://127.0.0.1:5000/ 

  - flask run --host=0.0.0.0:

  - http://192.168.1.155:5000/ 

#### Departments api:
 - GET /api/v1/departments - return all departments in json format
 
response: 200 OK

```json
[
    {
        "employee": [
            {
                "birthdate": "1962-08-11",
                "name": "Christopher Carroll",
                "salary": 854,
                "id": 6
            },
            {
                "birthdate": "1961-06-05",
                "name": "Brenda Mathis",
                "salary": 408,
                "id": 17
            },
            ...

        ],
        "name": "Management",
        "average_salary": 3933,
        "id": 1
    },
    {
        "employee": [
            {
                "birthdate": "1976-12-23",
                "name": "Maria Parker",
                "salary": 720,
                "id": 7
            },
            {
                "birthdate": "1976-01-08",
                "name": "Michelle Jacobs",
                "salary": 802,
                "id": 8
            },
            ...

        ],
        "name": "Sales",
        "average_salary": 6660,
        "id": 2
    }
]
```

 - POST /api/v1/departments - add a new department to the database (post request must be followed
 with json with the fields to add). Example:  

request:

```json
{
    "name": "New Department"
}
```

response: 201 CREATED or 400 BAD REQUEST

```json
{
    "employee": [],
    "name": "New Department",
    "average_salary": 0,
    "id": 6
}
```

- GET /api/v1/departments/*id* - return the department with the given id 
in json format

response: 200 OK or 404 NOT FOUND

```json
{
    "employee": [
        {
            "birthdate": "1976-12-23",
            "name": "Maria Parker",
            "salary": 720,
            "id": 7
        },
        {
            "birthdate": "2001-06-19",
            "name": "Bryce Harris",
            "salary": 573,
            "id": 53
        },
        ...
    ],
    "name": "Sales",
    "average_salary": 6660,
    "id": 2
}
```

- PUT /api/v1/departments/*id* - updates the department with the given id
with the values, provided in json format. Example:  

request:

```json
{
  "name": "Updated New Department"
}
```

response: 201 CREATED or 404 NOT FOUND or 400 BAD REQUEST

```json
{
    "average_salary": 0,
    "employee": [],
    "id": 6,
    "name": "Updated New Department"
}
```

- DELETE /api/v1/departments/*id*?orphan=0 - deletes the department with the given id, employee of this department will move to None department

response: 204 NO CONTENT or 404 NOT FOUND

- DELETE /api/v1/departments/*id*?orphan=1 - deletes the department with his employees by the given id 

response: 204 NO CONTENT or 404 NOT FOUND
   
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
