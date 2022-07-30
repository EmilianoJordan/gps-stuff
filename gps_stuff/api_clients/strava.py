from dataclasses import dataclass


@dataclass
class User:
    client_secret: str
    access_token: str
    refresh_token: str


class Strava:
    def __init__(self, user):
        self.user = user
