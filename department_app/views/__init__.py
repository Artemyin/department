from .department_view import department_bp
from .employee_view import employee_bp
from .index_view import index_bp
from .error_handler import page_not_found, internal_error


def init_app(app):
    """[summary]

    :param app: [description]
    :type app: [type]
    """
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(index_bp)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_error)
    