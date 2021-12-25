from .base import db, migrate


def init_app(app):
    """[summary]

    :param app: [description]
    :type app: [type]
    """
    db.init_app(app)
    migrate.init_app(app, db)