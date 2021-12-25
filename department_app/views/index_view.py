from os import name
from flask import Blueprint, jsonify,  render_template

from department_app.views.department_view import department


# Blueprint Configuration
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@index_bp.route('/', methods=['GET'])
def index():
    """Index view function for rendering 
    index page of application

    :return: render html template index.html
    :rtype: render_template()
    """
    return render_template("index.html")
