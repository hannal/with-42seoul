import pytest

from accounts.services import signup
from accounts.repositories import Repository


@pytest.fixture
def fixtures():
    storage_name = 'accounts.json'
    repository = Repository(storage_name)
    yield {
        'repository': repository,
    }
    repository.unlink_storage()


def test_유효한_ID와_PW를_제출하면_ID_PW를_저장하고_회원_가입_완료_응답을_한다(fixtures):
    repository = fixtures['repository']
    payload = {
        'username': 'test',
        'password': 'test',
    }

    result = signup(payload, repository)
    assert result['code'] == 201


def test_중복된_ID를_제출하면_중복_ID_오류_응답을_한다(fixtures):
    repository = fixtures['repository']
    payload = {
        'username': 'duplicated',
        'password': 'test',
    }
    result = signup(payload, repository)
    assert result['code'] == 201

    result = signup(payload, repository)
    assert result['code'] == 400
    assert result['reason'] == 'duplicated-username'
