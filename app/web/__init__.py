from flask import Blueprint
from .auth import LoginView

web = Blueprint(
    'web',
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='/web')

LoginView.register(web)
