from menubot import models
from menubot.models import schemas

from .sqlalchemy import SQLAlchemyRepository


class DateRepository(SQLAlchemyRepository):
    model = models.Dates
    schema = schemas.Date
