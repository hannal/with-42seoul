from accounts.services import signup


def test_유효한_ID와_PW를_제출하면_ID_PW를_저장하고_회원_가입_완료_응답을_한다():
    payload = {
        'username': 'test',
        'password': 'test',
    }

    result = signup(payload)
    assert result['code'] == 201
