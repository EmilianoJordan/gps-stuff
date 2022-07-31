from pathlib import Path

import pytest

from gps_stuff.config import Config


@pytest.fixture
def alembic_config(app):
    path = Path(app.root_path).parent
    return {
        "file": f"{path}/migrations/alembic.ini",
        "sqlalchemy.url": Config.SQLALCHEMY_DATABASE_URI,
        "script_location": f"{path}/migrations",
    }


@pytest.fixture
def alembic_engine(app):
    return app.extensions["migrate"].db.engine
