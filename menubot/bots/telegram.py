import logging

from aiogram import Bot, Dispatcher, executor, types  # type: ignore

from . import BaseBot


log = logging.getLogger(__name__)

class TelegramBot(BaseBot):
    def __init__(self, token: str) -> None:
        log.error("TODO")

        self._bot = Bot(token)
        self._dp = Dispatcher(self._bot)

        @self._dp.message_handler(commands=["start", "hello"])
        async def send_welcome(msg: types.Message):
            await msg.reply("hello world")

    def run(self):
        executor.start_polling(self._dp, skip_updates=True)
