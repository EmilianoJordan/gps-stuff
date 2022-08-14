import os

import click
from flask.cli import with_appcontext
from sqlalchemy.exc import IntegrityError


@click.group()
def gps():
    """Utilities specifically for `gps_stuff`."""


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
@click.option("-e", "--rwgps-email", default="", help="Strava Client ID of the User.")
@click.option("-p", "--rwgps-password", default="", help="Strava Secret of the User.")
@click.option(
    "-k", "--rwgps-api-key", default="", help="Strava Refresh Token of the User."
)
@with_appcontext
def add(
    first_name: str,
    last_name: str,
    rwgps_email: str,
    rwgps_password: str,
    rwgps_api_key: str,
):
    """ """
    _locals = locals().copy()

    from gps_stuff.app import db
    from gps_stuff.models import User

    values = _get_values(**_locals, read_env=True)

    db.session.add(User(**values))

    try:
        db.session.commit()
        click.echo(f"Added User {values}")
        return
    except IntegrityError as e:
        click.echo(f"User Exists with values {values}")
        click.echo(e)
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
