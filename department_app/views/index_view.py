from flask import Blueprint, render_template


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
