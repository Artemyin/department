from .department_rest import api_department_bp
from .employee_rest import api_employee_bp

 
def init_app(app):
   """Registring blueprints for rest services
   called from factory app id department_app.__init__.py
   """
   app.register_blueprint(api_department_bp, url_prefix='/api/v1')
   app.register_blueprint(api_employee_bp, url_prefix='/api/v1')


