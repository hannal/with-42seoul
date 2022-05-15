import datetime

import factory.fuzzy
from django.utils import timezone

from posts.models import PostingSchedule


def add_hour_to_time(target: datetime.time, hour: int) -> datetime.time:
    if target.hour == 23 or target.hour + hour >= 23:
        return target.replace(hour=23)
    return target.replace(hour=target.hour + hour)


class PostingScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostingSchedule

    user = factory.SubFactory('users.tests.factories.UserFactory')
    from_hour = factory.LazyFunction(
        lambda: factory.fuzzy.FuzzyDateTime(timezone.localtime()).fuzz().time(),
    )
    to_hour = factory.LazyAttribute(lambda o: add_hour_to_time(o.from_hour, 1))
