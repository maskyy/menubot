import logging
import logging.config

from .config import LOG_LEVEL


def setup_logger(level: int | str = LOG_LEVEL):
    logging.basicConfig(level=LOG_LEVEL)
