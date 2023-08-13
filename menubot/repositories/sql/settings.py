from sqlalchemy import update

from menubot import models
from menubot.models import schemas

from .sqlalchemy import SQLAlchemyRepository


class SettingsRepository(SQLAlchemyRepository):
    model = models.Settings
    schema = schemas.Settings

    def update(self, new: schemas.Settings) -> schemas.Settings:
        data = {"rowid": models.SETTINGS_ROWID}
        if new.first_date:
            data["first_date"] = new.first_date
        if new.days_count:
            data["days_count"] = new.days_count
        if new.owner:
            data["owner"] = new.owner

        session = self.session
        session.execute(update(self.model), data)
        session.commit()
        return self.get()

    def get(self) -> schemas.Settings | None:
        settings = self.session.get(self.model, models.SETTINGS_ROWID)
        if settings is None:
            return None
        return self._model_to_schema(settings)
