from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Interface abstrata para representar um planeador no contexto de um agente de planeamento.

    Esta interface serve como base para a implementação de diferentes tipos de planeadores, proporcionando uma estrutura comum.
    """
    @abstractmethod
    def planear(self, modelo_plan, objectivos): pass
