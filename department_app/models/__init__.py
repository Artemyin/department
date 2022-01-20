from .base import db, migrate


def init_app(app):
    """Registring database and migrations
    called from factory app id department_app.__init__.py
    :param app: flask application
    :type app: Flask
    """
    db.init_app(app)
    migrate.init_app(app, db)
