from .serializer import ma


def init_app(app):
    """[summary]

    :param app: [description]
    :type app: [type]
    """
    ma.init_app(app)
