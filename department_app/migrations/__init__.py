#from .manage import migrate, MIGRATION_DIR
import os
from department_app.models.base import db
from flask_migrate import Migrate

#MIGRATION_DIR = os.path.join('migrations')
#directory=MIGRATION_DIR

migrate = Migrate()

def init_app(app, db=db):
    migrate.init_app(app, db)
