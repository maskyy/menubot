import importlib
import logging

from ..config import BOT_CLASS
from . import BaseBot


log = logging.getLogger(__name__)


def get_bot(path: str = BOT_CLASS) -> BaseBot:
    if not path:
        raise ValueError("Please specify a bot class")

    try:
        path_list = path.split(".")
        bot_class = getattr(importlib.import_module(".".join(path_list[:-1])), path_list[-1])
        return bot_class()
    except Exception as exc:
        log.error(f"Cannot load bot {path}", exc_info=exc)
        raise
