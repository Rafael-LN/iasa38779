from abc import ABC, abstractmethod


class MecanismoProcura(ABC):
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
        
    def _iniciar_memoria(self): pass
    
    @abstractmethod
    def _memorizar(self, no): pass
    
    def procurar(self, problema): pass
    
    def _expandir(self, problema, no): pass