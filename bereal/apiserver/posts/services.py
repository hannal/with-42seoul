import typing as t
import datetime

from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone

from accounts.repositories import BaseRepository as BaseUserRepository
from posts.repositories import PostRepository

Listable: t.TypeAlias = QuerySet


class Notifier:
    _users: Listable[User] = None
    _success_users: list[User] = None
    _user_repository: BaseUserRepository = None
    _repository: PostRepository = None

    def __init__(
            self,
            target_time: datetime.datetime,
            user_repository: BaseUserRepository,
            repository: PostRepository,
    ):
        self.target_time = target_time
        self._user_repository = user_repository
        self._repository = repository

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
        if self._users is not None:
            return
        self._users = self._user_repository.collect_users_to_notify(self.target_time)

    def notify(self, limit_hour: int):
        self._success_users = []
        for _o in self.users:
            _time = timezone.localtime() + datetime.timedelta(hours=limit_hour)
            if not self._repository.has_timelimited_post(_o, _time):
                self._repository.create_timelimited_post(_o, _time)
            self._success_users.append(_o)
