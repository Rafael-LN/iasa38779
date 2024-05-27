import math
from pee.melhor_prim.heuristica import Heuristica

class HeurDist(Heuristica):
    """
    A classe HeurDist implementa uma heurística baseada na distância euclidiana entre o estado atual e o estado final.

    Atributos:
        __estado_final: Estado que representa o objetivo final do problema.

    Métodos:
        __init__(self, estado_final): Inicializa a instância da classe com o estado final objetivo.
        h(self, estado): Calcula a heurística (distância euclidiana) entre o estado atual e o estado final.
    """

    def __init__(self, estado_final):
        """
        Inicializa uma instância da classe HeurDist.

        Parâmetros:
            estado_final: Estado que representa o objetivo final do problema.

        Este método inicializa o atributo estado_final com o valor fornecido.
        """
        self.__estado_final = estado_final
        
    def h(self, estado):
        """
        Calcula a heurística (distância euclidiana) entre o estado atual e o estado final.

        Parâmetros:
            estado: O estado atual para o qual se deseja calcular a heurística.

        Retorna:
            float: A distância euclidiana entre o estado atual e o estado final.
        """
        return math.dist(self.__estado_final.posicao, estado.posicao)
