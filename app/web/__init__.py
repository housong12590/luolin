from flask import Blueprint
from .auth import AuthView

web = Blueprint(
    'web',
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='/web')

AuthView.register(web)

from flask import url_for

# print(url_for('web.AuthView:login'))
