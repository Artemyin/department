from .serializer import ma


def init_app(app):
    ma.init_app(app)
