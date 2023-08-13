from menubot import models
from menubot.models import schemas

from .sqlalchemy import SQLAlchemyRepository


class MenuImageRepository(SQLAlchemyRepository):
    model = models.MenuImages
    schema = schemas.MenuImage
