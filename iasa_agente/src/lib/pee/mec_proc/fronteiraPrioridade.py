from heapq import heappush, heappop
from pee.mec_proc.fronteira import Fronteira

class FronteiraPrioridade(Fronteira):
    """
    Classe que define uma fronteira de prioridade para armazenar nós de busca, onde o critério de prioridade é determinado por um avaliador.

    Attributes:
        __avaliador: O avaliador utilizado para determinar a prioridade dos nós.

    Métodos:
        inserir: Insere um nó na fronteira de acordo com sua prioridade.
        remover: Remove e retorna o nó com a maior prioridade da fronteira.
    """

    def __init__(self, avaliador):
        """
        Inicializa a fronteira de prioridade com o avaliador especificado.

        Args:
            avaliador: O avaliador utilizado para determinar a prioridade dos nós.
        """
        self.__avaliador = avaliador
        
    def inserir(self, no):
        """
        Insere um nó na fronteira de acordo com sua prioridade.

        Args:
            no: O nó a ser inserido na fronteira.
        """
        heappush(self._nos, no)
        
    def remover(self):
        """
        Remove e retorna o nó com a maior prioridade da fronteira.

        Retorno:
            O nó com a maior prioridade na fronteira.
        """
        return heappop(self._nos)
