from flask import Flask
from config import Config


# app = Flask(__name__)
#
# from app.errors import bp as errors_bp
#
# app.register_blueprint(errors_bp)
#
# from app import routes, models


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)

    @app.route('/')
    def index():
        return 'hello luolin'

    return app
