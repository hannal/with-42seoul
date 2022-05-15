import pytest
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.tests.factories import UserFactory
from accounts.repositories import DBRepository
from posts.services import Notifier
from posts.models import Post
from posts.repositories import PostRepository
from posts.tests.factories import PostingScheduleFactory


@pytest.mark.django_db
def test_정해진_시간_마다_무작위로_이용자를_선택하여_게시물을_작성하는_스케쥴러가_작동하는지_테스트():
    user_repository = DBRepository()
    post_repository = PostRepository(Post)

    # Given : 게시물 작성 시간대이 기준 시간을 포함하는 이용자 a는
    target_time = timezone.localtime()
    expected_users: list[User] = [
        UserFactory(),
    ]
    [
        PostingScheduleFactory(
            user=_o,
            from_hour=target_time.time(),
        )
        for _o in expected_users
    ]
    not_expected_users: list[User] = [
        UserFactory(),
    ]

    # When : 기준 시간에 게시물 작성 알림기가 실행되면
    notifier = Notifier(target_time, user_repository, post_repository)
    notifier.collect_users_to_notify()
    notifier.notify()

    # Then : 게시물 작성 알림을 받고,
    result = set([_o.username for _o in notifier.success_users])
    expected = set([_o.username for _o in expected_users])
    not_expected = set([_o.username for _o in not_expected_users])
    assert result == expected
    assert not (result & not_expected)

    # Then : 게시물 작성 제한 시간이 기록된다.
    result = [
        post_repository.has_timelimited_post(_o, target_time)
        for _o in expected_users
    ]
    assert len(result) == len(expected_users)
