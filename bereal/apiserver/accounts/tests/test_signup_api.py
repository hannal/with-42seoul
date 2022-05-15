import pytest

from accounts.repositories import Repository


@pytest.fixture
def fixtures():
    repository = Repository()
    yield {
        'repository': repository,
    }
    repository.unlink_storage()


def test_회원가입_성공_api(tp_api, fixtures):
    url = '/signup/'
    payload = {
        'username': 'test',
        'password': 'test',
    }
    res = tp_api.post(url, data=payload)
    assert res.status_code == 201
