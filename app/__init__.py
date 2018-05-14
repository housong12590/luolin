import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap3 import Bootstrap
from flask_session import Session as Redis_Session
from celery import Celery

db = SQLAlchemy()
session = Redis_Session()
bootstrap = Bootstrap()
migrate = Migrate()
celery = None


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)
    configure_extensions(app)
    configure_blueprints(app)
    configure_error_handlers(app)
    configure_logs(app)
    return app


def configure_extensions(app):
    global celery
    db.init_app(app)
    session.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    celery = Celery(
        app.name,
        broker=app.config['REDIS_URI'],
        backend=app.config['REDIS_URI']
    )
    celery.conf.update(app.config)


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
