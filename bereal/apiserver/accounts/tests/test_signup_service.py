import pytest

from accounts.services import signup
from accounts.repositories import FileRepository, DBRepository


@pytest.fixture
def fixtures():
    result = {
        'file_repository': FileRepository('accounts.json'),
        'db_repository': DBRepository(),
    }
    yield result
    result['file_repository'].unlink_storage()


repository_parametrize = pytest.mark.parametrize(
    'repository_key',
    [
        'file_repository',
        'db_repository',
    ]
)


@repository_parametrize
@pytest.mark.django_db
def test_유효한_ID와_PW를_제출하면_ID_PW를_저장하고_회원_가입_완료_응답을_한다(fixtures, repository_key):
    repository = fixtures[repository_key]
    payload = {
        'username': 'test',
        'password': 'test',
    }

    result = signup(payload, repository)
    assert result['code'] == 201


@repository_parametrize
@pytest.mark.django_db
def test_중복된_ID를_제출하면_중복_ID_오류_응답을_한다(fixtures, repository_key):
    repository = fixtures[repository_key]
    payload = {
        'username': 'duplicated',
        'password': 'test',
    }
    result = signup(payload, repository)
    assert result['code'] == 201

    result = signup(payload, repository)
    assert result['code'] == 400
    assert result['reason'] == 'duplicated-username'
