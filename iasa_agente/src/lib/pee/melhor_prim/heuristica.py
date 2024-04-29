from abc import ABC, abstractmethod


class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        pass