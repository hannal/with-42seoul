import typing as t
import json
from pathlib import Path

from django.contrib.auth import get_user_model
from django.db.models import Model


class BaseRepository:
    def unlink_storage(self):
        pass

    def create(self, payload: dict):
        raise NotImplementedError

    def find_by_username(self, username: str):
        raise NotImplementedError


class FileRepository(BaseRepository):
    _storage = None

    def __init__(self, storage: str = None):
        if not storage:
            storage = 'accounts.json'
        self._storage = storage

    @property
    def _storage_path(self) -> Path:
        return Path(self._storage).resolve()

    def _load_storage(self) -> list[dict]:
        if not self._storage_path.exists():
            self._storage_path.write_text('[]')
            return []

        with self._storage_path.open('r+') as fp:
            data = fp.read()
            if not data:
                return []
            return json.loads(data)

    def unlink_storage(self):
        self._storage_path.unlink(True)

    def create(self, payload: dict):
        if not payload:
            raise ValueError('Payload is required')

        data = self._load_storage()
        data.append(payload)
        with self._storage_path.open('w+') as fp:
            fp.write(json.dumps(data))
        return payload

    def find_by_username(self, username: str):
        data = self._load_storage()
        for _v in data:
            if _v.get('username') == username:
                return _v


class DBRepository(BaseRepository):
    model: Model = None

    def __init__(self, model: t.Optional[Model] = None):
        if not model:
            model = get_user_model()
        self.model = model

    @property
    def queryset(self, *args, **kwargs):
        return self.model.objects.filter(*args, **kwargs)

    def create(self, payload: dict):
        return self.model.objects.create_user(**payload)

    def find_by_username(self, username: str):
        return self.queryset.filter(username=username).first()
