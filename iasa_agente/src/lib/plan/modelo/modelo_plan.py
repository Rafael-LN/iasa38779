from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """
    Interface abstrata para representar um modelo de planeamento no contexto de um agente de planeamento.

    Métodos abstratos:
        obter_estado(self): Retorna o estado atual do modelo de planeamento.
        obter_estados(self): Retorna todos os estados válidos no modelo de planeamento.
        obter_operadores(self): Retorna todos os operadores válidos no modelo de planeamento.
    """
    
    @abstractmethod
    def obter_estado(self):
        """
        Método abstrato que deve ser implementado para retornar o estado atual do modelo de planeamento.

        Retorna:
            Estado atual do modelo de planeamento.
        """
        pass
    
    @abstractmethod
    def obter_estados(self):
        """
        Método abstrato que deve ser implementado para retornar todos os estados válidos no modelo de planeamento.

        Retorna:
            list: Lista de estados válidos.
        """
        pass
    
    @abstractmethod
    def obter_operadores(self):
        """
        Método abstrato que deve ser implementado para retornar todos os operadores válidos no modelo de planeamento.

        Retorna:
            list: Lista de operadores válidos.
        """
        pass
