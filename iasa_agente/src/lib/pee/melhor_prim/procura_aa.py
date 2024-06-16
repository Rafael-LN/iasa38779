from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraAA(ProcuraInformada):
    """
    Classe que implementa o algoritmo de procura A* (A Estrela).
    Herda da classe ProcuraInformada e utiliza o AvaliadorAA para determinar a prioridade dos nós com base na função de avaliação f(n) = g(n) + h(n).
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ProcuraAA.

        Funcionalidade:
        Este construtor chama o construtor da classe base ProcuraInformada, passando AvaliadorAA como o avaliador
        que será utilizado para calcular a prioridade dos nós durante a exploração.
        O AvaliadorAA combina o custo acumulado (g(n)) e a estimativa heurística (h(n)) para calcular a prioridade.
        """
        super().__init__(AvaliadorAA())
