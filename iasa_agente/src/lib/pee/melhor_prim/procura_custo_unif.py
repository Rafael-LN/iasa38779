from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Classe que implementa o algoritmo de procura de custo uniforme.

    Métodos:
        __init__: Inicializa a procura de custo uniforme com um avaliador de custo uniforme.
    """

    def __init__(self):
        """
        Inicializa a procura de custo uniforme com um avaliador de custo uniforme.
        """
        super().__init__(AvaliadorCustoUnif())
