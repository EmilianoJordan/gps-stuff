import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from gps_stuff.app import db


class User(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    rwgps_email = Column(String, nullable=False, unique=True)
    rwgps_password = Column(String, nullable=False)
    rwgps_api_key = Column(String, nullable=False, unique=True)
    rwgps_token = Column(String, nullable=True)
