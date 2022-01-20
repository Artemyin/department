from requests import request
from flask import render_template, Blueprint, jsonify


error_bp = Blueprint(
    'error_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@error_bp.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@error_bp.errorhandler(404)
def _handle_api_error(ex):
    if request.path.startwith('api/v1/'):
        return jsonify(ex)    
    else:
        return ex

def internal_error(error):
    return render_template('500.html'), 500

