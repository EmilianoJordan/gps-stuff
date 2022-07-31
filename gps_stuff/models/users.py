import uuid

from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from gps_stuff.app import db


class User(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    strava_client_id = Column(Integer, nullable=False)
    strava_secret = Column(String, unique=True, nullable=False)
    strava_refresh_token = Column(String)
    strava_token = Column(String)
    strava_token_expiration = Column(TIMESTAMP(timezone=True))
