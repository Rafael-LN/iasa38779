from abc import ABC, abstractmethod


class Problema(ABC):
    
    def __init__(self, estado_inicial, operadores):
        self.estado_inicial = estado_inicial
        self.operadores = operadores
        
    @abstractmethod
    def objectivo(self, estado): pass