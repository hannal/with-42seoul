import json
from pathlib import Path


class Repository:
    _storage = None

    def __init__(self, storage: str = None):
        if not storage:
            storage = 'accounts.json'
        self._storage = storage

    @property
    def _storage_path(self) -> Path:
        return Path(self._storage).resolve()

    def _load_storage(self) -> list[dict]:
        with open(self._storage, 'w+') as fp:
            data = fp.read()
            if not data:
                return []
            return json.loads(data)

    def unlink_storage(self):
        self._storage_path.unlink()

    def create(self, payload: dict):
        if not payload:
            raise ValueError('Payload is required')

        data = self._load_storage()
        data.append(payload)
        with open(self._storage, 'w') as fp:
            fp.write(json.dumps(data))
        return payload
