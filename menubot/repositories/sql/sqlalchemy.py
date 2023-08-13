from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from ...engine import engine as default_engine
from .. import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    model: type
    schema: type

    def __init__(self, engine: AsyncEngine = default_engine) -> None:
        self._engine = engine

    def _schema_to_model(self, s):
        return self.model(s.dict())

    @property
    def session(self) -> AsyncSession:
        return AsyncSession(self._engine)

    def create(self, item):
        self.session.add(self._schema_to_model(item))
        return item
