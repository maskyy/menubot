from menubot import models
from menubot.models import schemas

from . import SQLAlchemyRepository


class SettingsRepository(SQLAlchemyRepository):
    model = models.Settings
    schema = schemas.Settings

    def create(self, settings: schemas.Settings) -> schemas.Settings:
        self.session.add(settings)
        return settings

    def update(self, new: schemas.Settings) -> schemas.Settings:
        session = self.session
        current = session.query(model).get(rowid=models.SETTINGS_ROWID)
        # update TODO
