import logging

from .bots import get_bot_class
from .config import BOT_API_KEY
from .logger import setup_logger


log = logging.getLogger(__name__)


def main():
    setup_logger()
    # TODO setup DB, dates
    bot_class = get_bot_class()
    bot = bot_class(BOT_API_KEY)
    log.info(f"Running {bot}")

    bot.run()

if __name__ == "__main__":
    main()
