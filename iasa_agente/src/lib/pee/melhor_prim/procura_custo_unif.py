from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Classe que implementa o algoritmo de procura de custo uniforme.
    Herda da classe ProcuraMelhorPrim e utiliza um avaliador específico que considera o custo uniforme.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ProcuraCustoUnif.

        Funcionalidade:
        Este construtor chama o construtor da classe base ProcuraMelhorPrim, passando uma instância de AvaliadorCustoUnif.
        O AvaliadorCustoUnif é utilizado para avaliar os nós com base no custo acumulado do percurso, implementando a estratégia de procura de custo uniforme.
        """
        super().__init__(AvaliadorCustoUnif())
