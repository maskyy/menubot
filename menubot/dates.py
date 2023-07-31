import datetime

from .config import CURRENT_YEAR


DATE_FORMATS = ["%d-%m", "%d-%m-%Y", "%d.%m"]


def get_date(name: str) -> datetime.datetime:
    for fmt in DATE_FORMATS:
        try:
            date = datetime.datetime.strptime(name, fmt)
            break
        except ValueError:
            pass
    else:
        raise ValueError(f"Cannot parse {name} into a date")

    if date.year < CURRENT_YEAR:
        year = CURRENT_YEAR if date.month >= 9 else CURRENT_YEAR + 1
        date = date.replace(year=year)

    return date
