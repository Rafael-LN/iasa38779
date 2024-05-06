from abc import ABC, abstractmethod

class Heuristica(ABC):
    """
    Classe abstrata que define uma heurística para uso em algoritmos de busca informada.

    Métodos:
        h: Método abstrato para calcular o valor heurístico de um determinado estado.
    """

    @abstractmethod
    def h(self, estado):
        """
        Calcula o valor heurístico de um determinado estado.

        Args:
            estado: O estado para o qual o valor heurístico será calculado.

        Retorna:
            O valor heurístico do estado.
        """
        pass
