import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.dirname(__file__)
MIGRATION_DIR = os.path.join('migrations')
directory=MIGRATION_DIR

db = SQLAlchemy()
migrate = Migrate(directory=MIGRATION_DIR)