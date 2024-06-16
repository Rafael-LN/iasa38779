from pee.larg.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):
    """
    Classe que implementa o algoritmo de procura melhor-primeiro.
    Herda da classe ProcuraGrafo e utiliza uma fronteira de prioridade para a exploração dos nós, onde a prioridade é determinada por um avaliador.
    """

    def __init__(self, avaliador):
        """
        Inicializa uma nova instância de ProcuraMelhorPrim.

        Parâmetros:
        avaliador: O avaliador utilizado para calcular a prioridade dos nós.

        Funcionalidade:
        Este construtor chama o construtor da classe base ProcuraGrafo com uma fronteira de prioridade,
        utilizando o avaliador fornecido para determinar a prioridade dos nós.
        Também inicializa o atributo _avaliador com o avaliador fornecido.
        """
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    def _manter(self, no):
        """
        Determina se um nó deve ser mantido na fronteira de exploração.

        Parâmetros:
        no: O nó a ser avaliado.

        Retorna:
        True se o nó deve ser mantido, False caso contrário.

        Funcionalidade:
        Este método verifica se o nó deve ser mantido na fronteira de exploração.
        Um nó é mantido se ele ainda não foi explorado ou se o custo atual do nó é menor do que o custo registrado para o mesmo estado.
        """
        return super()._manter(no) or no.custo < self._explorados.get(no.estado).custo
