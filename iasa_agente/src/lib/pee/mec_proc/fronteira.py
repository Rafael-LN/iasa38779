from abc import ABC, abstractmethod


class Fronteira(ABC):
    
    def __init__(self):
        self._nos
        
    @property
    def vazia(self):
        return len(self._nos) == 0

    @property
    def dimensao(self):
        """
        Retorna a dimensão da estrutura de nós (fronteira)
        """
        return len(self._nos)
    
    def iniciar(self): pass
    
    @abstractmethod
    def inserir(self, no): pass
    
    def remover(self): pass