from menubot import models
from menubot.models import schemas

from . import SQLAlchemyRepository


class MenuTextRepository(SQLAlchemyRepository):
    model = models.MenuTexts
    schema = schemas.MenuText
