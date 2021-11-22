import os

class Config:
    NAME = "Base"

    _basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    DEVELOPMENT = False

    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    NAME = "Production"
    

class DevelopmentConfig(Config):
    NAME = "Development"
    DEBUG = True
    DEVELOPMENT = True