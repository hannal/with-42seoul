from accounts.repositories import Repository


def signup(payload: dict, repository: Repository) -> dict:
    account = repository.create({
        'username': payload['username'],
        'password': payload['password'],
    })

    return {
        'code': 201 if account else 500,
    }
