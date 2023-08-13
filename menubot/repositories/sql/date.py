from menubot import models
from menubot.models import schemas

from . import SQLAlchemyRepository


class DateRepository(SQLAlchemyRepository):
    model = models.Dates
    schema = schemas.Date
