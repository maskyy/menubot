from sqlalchemy import Engine
from sqlalchemy.orm import Session

from ...engine import engine as default_engine
from .. import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    model: type
    schema: type

    def __init__(self, engine: Engine = default_engine) -> None:
        self._engine = engine

    def _schema_to_model(self, s):
        return self.model(**s.dict())

    def _model_to_schema(self, m):
        data = {key: getattr(m, key, None) for key in m.__mapper__.attrs.keys()}
        return self.schema(**data)

    @property
    def session(self) -> Session:
        return Session(self._engine)

    def create(self, item):
        session = self.session
        session.add(self._schema_to_model(item))
        session.commit()
        return item
