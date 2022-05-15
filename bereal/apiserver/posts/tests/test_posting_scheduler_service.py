import pytest
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.tests.factories import UserFactory
from posts.services import Notifier


@pytest.mark.django_db
def test_정해진_시간_마다_무작위로_이용자를_선택하여_게시물을_작성하는_스케쥴러가_작동하는지_테스트():
    # Given : 게시물 작성 시간대이 기준 시간을 포함하는 이용자 a는
    target_time = timezone.localtime()
    expected_users: list[User] = [
        UserFactory(),
    ]
    not_expected_users: list[User] = [
        UserFactory(),
    ]

    # When : 기준 시간에 게시물 작성 알림기가 실행되면
    notifier = Notifier(target_time)
    notifier.collect_users_to_notify()
    notifier.notify()

    # Then : 게시물 작성 알림을 받고, 게시물 작성 제한 시간이 기록된다.
    result = set([_o.username for _o in notifier.success_users])
    expected = set([_o.username for _o in expected_users])
    assert result == expected
