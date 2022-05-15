import datetime

from django.contrib.auth.models import User


class Notifier:
    _users: list[User] = None
    _success_users: list[User] = None

    def __init__(self, target_time: datetime.datetime):
        self.target_time = target_time

    @property
    def users(self):
        if self._users is None:
            raise ValueError('Users not collected')
        return self._users

    @property
    def success_users(self):
        if self._success_users is None:
            raise ValueError('Notification not sent')
        return self._success_users

    def collect_users_to_notify(self):
        if self._users is None:
            self._users = []

    def notify(self):
        self._success_users = []
