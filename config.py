import os

class Config:
    """
    
    """
    NAME = "Base"
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    FLASK_APP = os.getenv("FLASK_APP", "app")
    SQLALCHEMY_DATABASE_URI = "sqlite:///department_db"
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    """[summary]

    """
    NAME = "Production"
    

class DevelopmentConfig(Config):
    """[summary]

    """
    NAME = "Development"
    DEBUG = True
    DEVELOPMENT = True