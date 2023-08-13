from menubot import models
from menubot.models import schemas

from .sqlalchemy import SQLAlchemyRepository


class AdminRepository(SQLAlchemyRepository):
    model = models.Admins
    schema = schemas.Admin
