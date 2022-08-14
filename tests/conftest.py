import pytest

from gps_stuff.app import create_app
from gps_stuff.models import User


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def user_value_dict():
    return {
        "first_name": "Bart",
        "last_name": "Simpson",
        "rwgps_email": "test@test.com",
        "rwgps_password": "123",
        "rwgps_api_key": "notAnAPIKey",
    }


@pytest.fixture
def user(user_value_dict):
    return User(**user_value_dict)


@pytest.fixture
def persisted_user(user, db_session):
    db_session.add(user)
    db_session.commit()
    return user
