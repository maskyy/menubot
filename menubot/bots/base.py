from abc import ABC, abstractmethod


class BaseBot(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        pass

    def run(self) -> None:
        pass
