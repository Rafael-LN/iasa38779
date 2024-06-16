from math import dist
from pee.melhor_prim.heuristica import Heuristica

class HeurDist(Heuristica):
    """
    Classe que implementa uma heurística baseada na distância euclidiana para o planeamento em espaços de estados.
    Herda da classe Heuristica e utiliza a distância euclidiana entre a posição de um estado atual e a posição do estado final como valor heurístico.
    """

    def __init__(self, estado_final):
        """
        Inicializa uma nova instância de HeurDist com o estado final desejado.

        Parâmetros:
        estado_final: O estado objetivo para o qual a heurística irá calcular a distância.

        Funcionalidade:
        Este construtor armazena o estado final fornecido para uso posterior no cálculo da heurística.
        """
        self.__estado_final = estado_final

    def h(self, estado):
        """
        Calcula o valor heurístico para um determinado estado com base na distância euclidiana até o estado final.

        Parâmetros:
        estado: O estado atual para o qual se pretende calcular o valor heurístico.

        Retorna:
        A distância euclidiana entre a posição do estado atual e a posição do estado final.

        Funcionalidade:
        Este método utiliza a função dist da biblioteca math para calcular a distância euclidiana entre a posição do estado atual e a posição do estado final armazenado.
        """
        return dist(self.__estado_final.posicao, estado.posicao)
