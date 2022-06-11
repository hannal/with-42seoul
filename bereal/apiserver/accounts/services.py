from accounts.repositories import RepositoryType


def signup(payload: dict, repository: RepositoryType) -> dict:
    account = repository.find_by_username(payload['username'])
    if account:
        return {
            'code': 400,
            'reason': 'duplicated-username',
        }

    account = repository.create(payload)

    return {
        'code': 201 if account else 500,
    }
