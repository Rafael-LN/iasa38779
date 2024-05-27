from abc import ABC, abstractmethod

class Plano(ABC):
    """
    Interface abstrata para representar um plano no contexto de um agente de planeamento.

    Métodos abstratos:
        obter_accao(self, estado): Retorna a ação a ser tomada para um determinado estado.
        mostrar(self, vista): Exibe ou apresenta o plano em uma determinada visão.
    """

    @abstractmethod
    def obter_accao(self, estado):
        """
        Método abstrato que deve ser implementado para retornar a ação a ser tomada para um determinado estado.

        Parâmetros:
            estado: O estado atual para o qual se deseja obter a ação.

        Retorna:
            Ação a ser tomada no estado fornecido.
        """
        pass
    
    @abstractmethod
    def mostrar(self, vista):
        """
        Método abstrato que deve ser implementado para exibir ou apresentar o plano em uma determinada visão.

        Parâmetros:
            vista: A visão ou contexto em que o plano deve ser apresentado.
        """
        pass
