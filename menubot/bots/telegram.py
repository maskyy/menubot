import logging

from aiogram import Bot, Dispatcher, executor, types  # type: ignore

from . import BaseBot


log = logging.getLogger(__name__)

class TelegramBot(BaseBot):
    def __init__(self, token: str) -> None:
        super().__init__()
        log.error("TODO")

        self._bot = Bot(token)
        self._dp = Dispatcher(self._bot)

        for func, cmds in (self._commands | self._admin_commands).items():
            self._dp.register_message_handler(func, commands=cmds)

    def run(self):
        executor.start_polling(self._dp, skip_updates=True)

    async def menu(self, msg: types.Message):
        args = msg.get_args()
        d = None
        if args:
            d = args.split(maxsplit=1)[0]
            log.info(d)
        await msg.answer(f"hello {d}")

    async def settings(self, msg: types.Message):
        args = msg.get_args()
        await msg.answer(self._settings_service.settings(args))
