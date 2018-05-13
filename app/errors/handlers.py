from app.errors import blueprint
from flask import render_template


@blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@blueprint.app_errorhandler(500)
def internal_error():
    return render_template('errors/500.html'), 500
