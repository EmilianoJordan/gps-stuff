from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from gps_stuff.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from gps_stuff import models  # noqa:F401

    db.init_app(app)
    migrate.init_app(app)
