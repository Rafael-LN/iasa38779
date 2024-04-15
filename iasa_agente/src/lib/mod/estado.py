from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def id_valor(self):
        pass

    def __eq__(self, outro):
        return isinstance(outro, Estado) and self.id_valor() == outro.id_valor()

    def __hash__(self):
        return hash(self.id_valor())