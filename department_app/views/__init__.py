from .department_view import department_bp
from .employee_view import employee_bp
from .index_view import index_bp


def init_app(app):
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(index_bp)