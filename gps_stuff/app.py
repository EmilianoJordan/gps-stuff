from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from gps_stuff import cli, config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from gps_stuff import models

    register_extensions(app)
    register_shellcontext(app, models)
    register_cli(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shellcontext(app, models):
    from gps_stuff import models

    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {"db": db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, "__bases__") and db.Model in getattr(model, "__bases__"):
                ctx[attr] = model
        return ctx


def register_cli(app):
    app.cli.add_command(cli.gps)
