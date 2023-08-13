from abc import ABC, abstractmethod

from menubot.dates import get_date, today


class BaseBot(ABC):
    def __init__(self) -> None:
        self._commands = {
            self.menu: ["menu", "меню"],
            self.help: ["help", "помощь"],
        }

        self._admin_commands = {
            self.include_date: ["include_date"],
            self.exclude_date: ["exclude_date"],
            self.clear_dates: ["clear_dates"],
            self.list_dates: ["list_dates"],
            self.settings: ["settings"],
            self.parse_menu_images: ["update_menu"],
        }

    @abstractmethod
    def run(self) -> None:
        pass

    async def menu(self, date_str: str | None):
        today() if date_str is None else get_date(date_str)

    #@abstractmethod
    async def help(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def include_date(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def exclude_date(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def clear_dates(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def list_dates(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def settings(self, *args, **kwargs):
        pass

    #@abstractmethod
    async def parse_menu_images(self, *args, **kwargs):
        pass
