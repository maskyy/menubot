from pydantic import ValidationError

from menubot.models import schemas
from menubot.repositories.sql import SettingsRepository


class SettingsService:
    def __init__(self):
        self._repository = SettingsRepository()

    def settings(self, args: str | None) -> str:
        s = self._repository.get()
        if not args:
            if s is None:
                return "Settings not set. Please enter first_date, days_count, owner"
            return str(s)

        try:
            first_date, days_count, owner = args.split(maxsplit=3)[0:3]
        except ValueError:
            return "Not enough arguments"

        try:
            new = schemas.Settings(first_date=first_date, days_count=days_count, owner=owner)
            if s is None:
                return self._repository.create(new)
            return self._repository.update(new)
        except ValidationError as e:
            return str(e)
