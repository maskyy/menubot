from abc import ABC, abstractmethod


class BaseBot(ABC):
    @abstractmethod
    def __init__(self, token: str) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
