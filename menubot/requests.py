import asyncio
import logging

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from bs4.element import Tag

from .config import COLLEGE_HOST, MENU_PATH
from .dates import get_date


log = logging.getLogger(__name__)


async def get_name_and_link(li: Tag) -> tuple[str, str]:
    date = li.text.strip()
    a = list(li.children)[1]
    return date, a["href"]


async def get_menu_items(session: ClientSession) -> list[Tag]:
    async with session.get(MENU_PATH) as response:
        html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("li", class_="jpeg")


async def parse_and_query(session: ClientSession, elements: list[Tag]) -> None:
    tasks = [get_name_and_link(el) for el in elements]
    return await asyncio.gather(*tasks)


async def test():
    async with ClientSession(base_url=COLLEGE_HOST) as session:
        links = await get_menu_items(session)
        results = await parse_and_query(session, links)
    dates = [get_date(p[0]) for p in results]
    log.error(dates)


if __name__ == "__main__":
    asyncio.run(test())
