from flask import Blueprint

blueprint = Blueprint('errors', __name__)

from app.web.errors import handlers
