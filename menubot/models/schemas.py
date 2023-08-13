from datetime import date, datetime

from orjson import dumps, loads
from pydantic import BaseModel, HttpUrl


def dumps2(obj, *, default) -> str:
    return dumps(obj, default=default).decode()


class CustomBaseModel(BaseModel):
    class Config:
        json_dumps = dumps2
        json_loads = loads


class MenuImage(CustomBaseModel):
    id: int | None = None
    url: HttpUrl
    image: bytes
    file_id: str | None
    date: datetime



class Date(CustomBaseModel):
    id: int | None = None
    date: datetime
    included: bool


class MenuText(CustomBaseModel):
    id: int | None = None
    day: int
    text: str


class Admin(CustomBaseModel):
    id: int


class Settings(CustomBaseModel):
    first_date: date | None
    days_count: int | None
    owner: int | None
