"""
from flask import url_for, redirect, render_template, request, abort
from department_app import app, db
from department_app.service import EmployeeService, DepartmentService

# Flask views
@app.route('/')
def index():
    #all_emps = EmployeeService.get_all()
    return "Hello"
"""