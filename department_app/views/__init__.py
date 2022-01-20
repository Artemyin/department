from .department_view import department_bp
from .employee_view import employee_bp
from .index_view import index_bp
from .error_handler import error_bp, internal_error


def init_app(app):
    """Registring blueprints for view controler services
    called from factory app id department_app.__init__.py
    """
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(error_bp)
    app.register_error_handler(500, internal_error)


    