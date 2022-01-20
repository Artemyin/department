from flask import render_template, Blueprint


error_bp = Blueprint(
    'error_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@error_bp.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

