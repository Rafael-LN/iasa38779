from abc import ABC, abstractmethod

class Heuristica(ABC):
    """
    Classe abstrata que define a interface para funções heurísticas utilizadas em algoritmos de procura.
    Uma função heurística fornece uma estimativa do custo restante para atingir o objetivo a partir de um determinado estado.
    """

    @abstractmethod
    def h(self, estado):
        """
        Calcula a estimativa heurística para um determinado estado.

        Parâmetros:
        estado: O estado para o qual se pretende calcular a estimativa heurística.

        Retorna:
        A estimativa heurística do custo restante para atingir o objetivo a partir do estado fornecido.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a lógica de cálculo da heurística.
        A função heurística é utilizada para guiar a exploração do espaço de estados, ajudando a focar nos nós mais promissores.
        """
        pass
