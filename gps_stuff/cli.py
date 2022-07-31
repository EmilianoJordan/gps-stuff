import os

import click
from flask.cli import with_appcontext
from sqlalchemy.exc import IntegrityError


@click.group()
def gps():
    """Utilities specifically for `gps_stuff`."""
    pass


@gps.group()
def user():
    """Utilities for database User interactions"""


@user.command()
@click.option(
    "-f", "--first-name", default="", help="First name of the user to be added."
)
@click.option(
    "-l", "--last-name", default="", help="Last name of the user to be added."
)
@click.option(
    "-i", "--strava-client-id", default=0, help="Strava Client ID of the User."
)
@click.option("-s", "--strava-secret", default="", help="Strava Secret of the User.")
@click.option(
    "-r", "--strava-refresh-token", default="", help="Strava Refresh Token of the User."
)
@with_appcontext
def add(
    first_name: str,
    last_name: str,
    strava_client_id: int,
    strava_secret: str,
    strava_refresh_token: str,
):
    """ """
    _locals = locals().copy()

    from gps_stuff.app import db
    from gps_stuff.models import User

    values = _get_values(**_locals, read_env=True)

    db.session.add(User(**values))

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    values = _get_values(**_locals, read_env=False)

    db.session.add(User(**values))
    db.session.commit()


def _get_values(read_env=False, **kwargs):
    kwarg_generator = ((k, v) for k, v in kwargs.items() if not v)

    if read_env:

        for key, value in kwarg_generator:

            if val := os.environ.get(key.upper()):
                kwargs[key] = val
            else:
                kwargs[key] = click.prompt(f'User "{key}"', type=type(value))

        return kwargs

    else:

        for key, value in kwarg_generator:
            kwargs[key] = click.prompt(f'User "{key}"', type=type(value))

        return kwargs
