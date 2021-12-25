from .department_rest import api_department_bp
from .employee_rest import api_employee_bp

 
def init_app(app):
   """[summary]

   :param app: [description]
   :type app: [type]
   """
   app.register_blueprint(api_department_bp, url_prefix='/api/v1')
   app.register_blueprint(api_employee_bp, url_prefix='/api/v1')


