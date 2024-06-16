from pee.mec_proc.no import No
from pee.prof.procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Classe que implementa o algoritmo de procura em profundidade limitada.
    Herda da classe ProcuraProfundidade e adiciona uma profundidade máxima para limitar a expansão dos nós.
    """

    def __init__(self, prof_max):
        """
        Inicializa uma nova instância de ProcuraProfLim.

        Parâmetros:
        prof_max: A profundidade máxima permitida para a expansão dos nós.

        Funcionalidade:
        Este construtor inicializa a profundidade máxima e chama o construtor da classe base ProcuraProfundidade.
        """
        super().__init__()
        self.__prof_max = prof_max

    @property
    def prof_max(self):
        """
        Obtém a profundidade máxima permitida para a expansão dos nós.

        Retorna:
        A profundidade máxima.

        Funcionalidade:
        Este método retorna o valor da profundidade máxima permitida para a expansão dos nós.
        """
        return self.__prof_max

    @prof_max.setter
    def prof_max(self, prof_max):
        """
        Define a profundidade máxima permitida para a expansão dos nós.

        Parâmetros:
        prof_max: A nova profundidade máxima.

        Funcionalidade:
        Este método define um novo valor para a profundidade máxima permitida para a expansão dos nós.
        """
        self.__prof_max = prof_max

    def _expandir(self, problema, no):
        """
        Expande um nó, gerando seus sucessores, respeitando a profundidade máxima.

        Parâmetros:
        problema: O problema de planeamento que define os operadores.
        no: O nó a ser expandido.

        Retorna:
        Um gerador de nós sucessores.

        Funcionalidade:
        Este método expande o nó apenas se a sua profundidade for menor do que a profundidade máxima permitida.
        Utiliza o método de expansão da classe base para gerar os sucessores.
        """
        if no.profundidade < self.prof_max:
            yield from super()._expandir(problema, no)
