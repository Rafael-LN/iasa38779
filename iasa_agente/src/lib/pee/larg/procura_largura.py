from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.larg.procura_grafo import ProcuraGrafo

class ProcuraLargura(ProcuraGrafo):
    """
    Classe que implementa o algoritmo de procura em largura.
    Herda da classe ProcuraGrafo e utiliza uma fronteira FIFO (First In, First Out) para a exploração dos nós.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ProcuraLargura.

        Funcionalidade:
        Este construtor chama o construtor da classe base ProcuraGrafo com uma fronteira FIFO,
        garantindo que a exploração dos nós segue uma estratégia de primeiro a entrar, primeiro a sair (FIFO).
        A estratégia FIFO é típica de algoritmos de procura em largura, onde os nós mais antigos são explorados primeiro.
        """
        super().__init__(FronteiraFIFO())
