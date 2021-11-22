import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_marshmallow import Marshmallow
from flask import url_for, redirect, render_template, request, abort

def create_app():
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    from department_app import models
    models.init_app(app)

    from .serializers import ma
    ma.init_app(app)
    
    from department_app.models import db
    migrate = Migrate()
    migrate.init_app(app, db)
    
    
    from .service.departement_service import DepartmentService

    @app.route('/')
    def index():
        emps = DepartmentService.get_all()
        emp = emps[0].name
        config = app.config.get("NAME")
        return emp

    return app
