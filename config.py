import os

class Config:
    """
    
    """
    NAME = "Base"
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    FLASK_APP = os.getenv("FLASK_APP", "department_app")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or 'sqlite:///department_db'
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    """Production config
    Use for production deployment
    """
    NAME = "Production"
    

class DevelopmentConfig(Config):
    """Development config
    Use for development, DEBUG active
    """
    NAME = "Development"
    DEBUG = True
    DEVELOPMENT = True