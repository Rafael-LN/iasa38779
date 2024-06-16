from pee.larg.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):
    """
    Classe que define o comportamento de uma procura utilizando a estratégia de Melhor-Prim.

    Herda de ProcuraGrafo.

    Métodos:
        __init__: Método de inicialização que define o avaliador a ser utilizado na procura.
        _manter: Método para determinar se um nó deve ser mantido na memória durante a procura.
    """

    def __init__(self, avaliador):
        """
        Inicializa a procura com o avaliador especificado.

        Args:
            avaliador: O avaliador a ser utilizado na procura.
        """
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
        
    def _manter(self, no):
        """
        Determina se um nó deve ser mantido na memória durante a procura.

        Este método é abstrato e deve ser implementado pelas subclasses.

        Args:
            no: O nó a ser verificado.

        Returns:
            True se o nó deve ser mantido, False caso contrário.
        """
        return super()._manter(no) or no.custo < self._explorados.get(no.estado).custo