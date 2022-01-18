import os

class Config:
    """[summary]
    """
    NAME = "Base"
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    DEVELOPMENT = False
    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    FLASK_APP = os.getenv("FLASK_APP", "app")
    SQLALCHEMY_DATABASE_URI = "sqlite:///department_db"
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    """[summary]

    :param Config: [description]
    :type Config: [type]
    """
    NAME = "Production"
    

class DevelopmentConfig(Config):
    """[summary]

    :param Config: [description]
    :type Config: [type]
    """
    NAME = "Development"
    DEBUG = True
    DEVELOPMENT = True