from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    Classe abstrata que define a interface para avaliadores utilizados em algoritmos de procura.
    Um avaliador é responsável por determinar a prioridade de um nó durante a exploração do espaço de estados.
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato para calcular a prioridade de um nó.

        Parâmetros:
        no: O nó cuja prioridade será calculada.

        Retorna:
        A prioridade do nó, utilizada para ordenar a fronteira de exploração em algoritmos de procura.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a lógica de cálculo da prioridade de um nó.
        A prioridade é utilizada para determinar a ordem de exploração dos nós na fronteira de exploração.
        """
        pass
