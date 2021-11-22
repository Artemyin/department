import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    from department_app.models import db
    db.init_app(app)

    from .serializers import ma
    ma.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)
    

