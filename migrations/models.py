from sqlalchemy import BLOB, Boolean, Column, Integer, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class MenuImages(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    image = Column(BLOB, nullable=False)
    file_id = Column(Text)
    date = Column(Text, nullable=False)


class Dates(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True)
    date = Column(Text, nullable=False)
    included = Column(Boolean, nullable=False)


class MenuTexts(Base):
    __tablename__ = "menu_texts"

    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False, unique=True)
    text = Column(Text, nullable=False)


class Admins(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)


class Settings(Base):
    __tablename__ = "settings"

    # rowid should not be in the migrations
    rowid = Column(Integer, primary_key=True)
    first_date = Column(Text, nullable=False)
    days_count = Column(Integer, nullable=False)
    owner = Column(Integer, nullable=False)
