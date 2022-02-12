import os
os.environ['DATABASE_URL'] = 'sqlite://'

import unittest
from flask import current_app
from department_app import create_app
from department_app.models.base import db
from departmnet_app.models.department_model import Department
from departmnet_app.models.employee_model import Employee


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.populate_db()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def populate_db(self):
        employees = []
        departments = []
        employee1 = Employee(
            name="Artemii Noskov", 
            department="1", 
            salary=100, 
            birthdate="1994-01-04"
        )
        employees.append(employee1)
        department1 = Department(name="hr")
        departments.append(department1)
        for emploee in employees:
            db.session.add(employee)
        for department in departments:
            db.session.add(department)
        db.session.commit()
    
    def test_api_get_departments(self):
        response = self.client.get('/api/v1/departments')
        assert response.status_code == 200
        assert len(response.json) == 1
        assert response.json[0]['name'] == "hr"
