import typing as t
import datetime

from django.contrib.auth.models import User

from posts.models import Post


class PostRepository:
    model: t.Type[Post] = None

    def __init__(self, model: t.Type[Post]):
        self.model = model

    @property
    def queryset(self, *args, **kwargs):
        return self.model.objects.filter(*args, **kwargs)

    def has_timelimited_post(self, user: User, frozen_at: datetime.datetime):
        return self.queryset.filter(user=user, frozen_at__date=frozen_at.date()).exists()

    def create_timelimited_post(self, user: User, frozen_at: datetime.datetime):
        if self.has_timelimited_post(user, frozen_at):
            raise ValueError('Post already exists')
        return self.queryset.create(user=user, updated_at=None, frozen_at=frozen_at)
