from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraSofrega(ProcuraInformada):
    """
    Classe que implementa o algoritmo de procura Sôfrega (Greedy Search).
    Herda da classe ProcuraInformada e utiliza o AvaliadorSof para determinar a prioridade dos nós com base na heurística.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ProcuraSofrega.

        Funcionalidade:
        Este construtor chama o construtor da classe base ProcuraInformada, passando AvaliadorSof como o avaliador
        que será utilizado para calcular a prioridade dos nós durante a exploração.
        """
        super().__init__(AvaliadorSof())
