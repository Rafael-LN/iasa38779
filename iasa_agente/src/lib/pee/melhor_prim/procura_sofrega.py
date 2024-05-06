from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):
    """
    Classe que implementa o algoritmo de procura sofrega.

    Herda de ProcuraInformada.

    Atributos:
        Nenhum atributo adicional além dos herdados de ProcuraInformada.

    Métodos:
        __init__: Inicializa a classe, especificando o avaliador a ser usado.
    """

    def __init__(self):
        """
        Inicializa a procura sofrega com o AvaliadorSof.
        """
        super().__init__(AvaliadorSof)
