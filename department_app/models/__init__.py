from .base import db, migrate


def init_app(app):
    """Registring database and migrations 
    called from factory app id department_app.__init__.py

    :param app: [description]
    :type app: [type]
    """
    db.init_app(app)
    migrate.init_app(app, db)
