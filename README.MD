try me: https://murmuring-wildwood-38659.herokuapp.com/

#### Structure of project

department-app (a project / app directory)

- migrations (this package include migration files to manage database schema changes )

- models (this package include modules with Python classes describing DB models)

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
        "average_salary": 561.86,
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
        "average_salary": 475.71,
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
    "average_salary": 475.71,
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

response: 200 OK

```json
{
    "data": [
        {
            "salary": 1000,
            "birthdate": "1994-01-04",
            "department": {
                "id": 3,
                "name": "Engineering"
            },
            "id": 1,
            "name": "Artemii Noskov"
        },
        {
            "salary": 854,
            "birthdate": "1962-08-11",
            "department": {
                "id": 1,
                "name": "Management"
            },
            "id": 6,
            "name": "Christopher Carroll"
        },
        ...

    ],
    "recordsFiltered": 50,
    "recordsTotal": 50,
    "draw": null
}
```

 - POST /api/v1/employees - add a new employee to the database (post request must be followed
 with json with the fields to add). Example:  
 
request:

```json
{
    "name": "Artemii Noskov",
    "department": 3,
    "salary": 9999,
    "birthdate": "1994-01-04"
}
```

response: 201 CREATED or 400 BAD REQUEST

```json
{
    "salary": 9999,
    "birthdate": "1994-01-04",
    "department": {
        "id": 3,
        "name": "Engineering"
    },
    "id": 55,
    "name": "Artemii Noskov"
}
```

- GET /api/v1/employees/*id* - return the employee with the given id 
in json format

response: 200 OK or 404 NOT FOUND

```json
{
    "salary": 408,
    "birthdate": "1961-06-05",
    "department": {
        "id": 1,
        "name": "Management"
    },
    "id": 17,
    "name": "Brenda Mathis"
}
```

- PUT /api/v1/employees/*id* - updates the employee with the given id
with the values, provided in json format. Example:  
 
request:

```json
{
    "name": "Artemii Noskov",
    "department": 4,
    "salary": 1111,
    "birthdate": "1994-01-04"
}
```

response: 201 CREATED or 404 NOT FOUND or 400 BAD REQUEST

```json
{
    "salary": 1111,
    "birthdate": "1994-01-04",
    "department": {
        "id": 4,
        "name": "Service"
    },
    "id": 55,
    "name": "Artemii Noskov"
}
```


- DELETE /api/v1/employees/*id* - deletes the employee with the given id  

response: 204 NO CONTENT or 404 NOT FOUND


- GET /api/v1//employees/?start_date=1989-01-03&end_date=2021-09-23&department_id=2&search%5Bvalue%5D=r

search employees born on a specific date range, specific department, and by name

  -  start_date=<Y-m-d> - filter employyes from cpecific date in 'Year-month-day' format date, default value is '1900-1-1' 
  -  end_date=<Y-m-d> - filter employyes to cpecific date in 'Year-month-day' format date , default value is 'now'
  -  department_id=<department id: int> - fliter employyes for certain department, used in department view /departments/<id>
  -  search[value]=<name> search employees with name LIKE this.

response: 200 OK or 404 NOT FOUND

 ```json
{
    "data": [
        {
            "salary": 349,
            "birthdate": "1989-06-10",
            "department": {
                "id": 2,
                "name": "Sales"
            },
            "id": 11,
            "name": "Ronald Duke"
        },
        {
            "salary": 573,
            "birthdate": "2001-06-19",
            "department": {
                "id": 2,
                "name": "Sales"
            },
            "id": 53,
            "name": "Bryce Harris"
        }
    ],
    "recordsFiltered": 2,
    "recordsTotal": 51,
    "draw": null
}
```

#### Here is the list of available addresses of web application:

 
 #### Departments

 - /departments - display all the departments
 - /departments/*id* - display certain department by id
   
   
#### Employees

 - /employees - display all the employees
 - /employees/*id* - display certain employee by id
