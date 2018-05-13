import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import flask.globals

migrate = Migrate()
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)
    configure_extensions(app)
    configure_blueprints(app)
    configure_error_handlers(app)
    configure_logs(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)


def configure_blueprints(app):
    pass


def configure_error_handlers(app):
    pass


def configure_logs(app):
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/luolin.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')


from app import models
