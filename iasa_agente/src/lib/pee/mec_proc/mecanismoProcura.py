from abc import ABC, abstractmethod


class MecanismoProcura(ABC):
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
        self.__nos_processados = 0
    
    @property
    def nos_processados(self):
        return self.__nos_processados
    
    @property
    @abstractmethod
    def nos_memoria(self):
        """
        Obter número máximo de nós em memória
        """
        
    def _iniciar_memoria(self): pass
    
    @abstractmethod
    def _memorizar(self, no): pass
    
    def procurar(self, problema): pass
    
    def _expandir(self, problema, no): pass