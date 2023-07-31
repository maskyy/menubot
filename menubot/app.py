import logging

from .bots import get_bot
from .logger import setup_logger


log = logging.getLogger(__name__)


async def main():
    setup_logger()
    # TODO setup DB, dates
    bot = get_bot()
    log.info(f"Running {bot}")
    bot.run()
