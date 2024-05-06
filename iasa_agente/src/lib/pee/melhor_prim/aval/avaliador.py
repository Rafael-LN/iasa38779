from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    Classe abstrata que define um avaliador para determinar a prioridade de um nó.

    Métodos:
        prioridade: Método abstrato para calcular a prioridade de um nó.
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Calcula a prioridade de um nó durante a procura.

        Args:
            no: O nó para o qual a prioridade deve ser calculada.

        Returns:
            A prioridade do nó.
        """
        pass
