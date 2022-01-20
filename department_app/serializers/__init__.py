from .serializer import ma


def init_app(app):
    """Registring marshmellow schemas
    for serializtion, deserializtion, validation
    """
    ma.init_app(app)
