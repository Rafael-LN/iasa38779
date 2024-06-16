from heapq import heappush, heappop
from pee.mec_proc.fronteira import Fronteira

class FronteiraPrioridade(Fronteira):
    """
    Classe que implementa uma fronteira de prioridade para algoritmos de procura.
    Herda da classe Fronteira e utiliza uma heap (fila de prioridade) para ordenar os nós com base na sua prioridade.
    """

    def __init__(self, avaliador):
        """
        Inicializa uma nova instância de FronteiraPrioridade.

        Parâmetros:
        avaliador: O avaliador utilizado para calcular a prioridade dos nós.

        Funcionalidade:
        Este construtor chama o construtor da classe base Fronteira e inicializa o atributo __avaliador com o avaliador fornecido.
        """
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        """
        Insere um nó na fronteira de exploração utilizando a prioridade calculada pelo avaliador.

        Parâmetros:
        no: O nó a ser inserido na fronteira.

        Funcionalidade:
        Este método calcula a prioridade do nó utilizando o avaliador e insere o nó na heap, mantendo a ordem de prioridade.
        A heap garante que o nó com a menor prioridade será removido primeiro.
        """
        prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    def remover(self):
        """
        Remove e retorna o nó com a menor prioridade da fronteira de exploração.

        Retorna:
        O nó com a menor prioridade.

        Funcionalidade:
        Este método remove e retorna o nó com a menor prioridade da heap, garantindo que a exploração siga a ordem de prioridade.
        """
        (_, no) = heappop(self._nos)
        return no
