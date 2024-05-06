from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraAA(ProcuraInformada):
    """
    Classe que implementa o algoritmo de procura A*.

    Métodos:
        __init__: Inicializa a procura A* com um avaliador A*.
    """

    def __init__(self):
        """
        Inicializa a procura A* com um avaliador A*.
        """
        super().__init__(AvaliadorAA())
