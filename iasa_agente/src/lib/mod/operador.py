from abc import ABC, abstractmethod


class Operador(ABC):
    
    @abstractmethod
    def aplicar(self, estado): pass
    
    @abstractmethod
    def custo(self, estado, estado_suc): pass