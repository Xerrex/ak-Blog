from flask import render_template, Blueprint
from my_core.utils.extensions import db



error_bp = Blueprint('error', __name__)


@error_bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@error_bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
