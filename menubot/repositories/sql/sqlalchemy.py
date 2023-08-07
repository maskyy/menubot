from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from ...engine import engine as default_engine
from .. import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    def __init__(self, engine: AsyncEngine = default_engine) -> None:
        self._engine = engine
        self._session = AsyncSession(self._engine)

    def __del__(self):
        self._session.commit()
        self._session.close()
