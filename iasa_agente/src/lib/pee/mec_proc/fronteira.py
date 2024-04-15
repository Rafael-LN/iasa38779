from abc import ABC, abstractmethod


class Fronteira(ABC):
    
    def __init__(self):
        self._nos
        self.vazia
    
    def iniciar(self): pass
    
    @abstractmethod
    def inserir(self, no): pass
    
    def remover(self): pass