from pee.mec_proc.no import No
from pee.prof.procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Classe que implementa um mecanismo de procura em profundidade limitada.

    Métodos:
        __init__: Inicializa a busca em profundidade limitada com a profundidade máxima especificada.
        prof_max: Propriedade para obter ou definir a profundidade máxima de busca.
        _expandir: Expande um nó durante a busca, considerando a profundidade máxima.
    """

    def __init__(self, prof_max):
        """
        Inicializa a busca em profundidade limitada com a profundidade máxima especificada.

        Args:
            prof_max: A profundidade máxima de busca.
        """
        self.prof_max = prof_max
        
    @property
    def prof_max(self):
        """
        Propriedade para obter a profundidade máxima de busca.

        Retorno:
            A profundidade máxima de busca.
        """
        return self._prof_max

    @prof_max.setter
    def prof_max(self, prof_max):
        """
        Propriedade para definir a profundidade máxima de busca.

        Args:
            prof_max: A profundidade máxima de busca.
        """
        self._prof_max = prof_max
    
    def _expandir(self, problema, no):
        """
        Expande um nó durante a procura em profundidade limitada.

        Args:
            problema: O problema a ser resolvido.
            no: O nó a ser expandido durante a procura.

        Retorno:
            Uma lista de nós sucessores gerados pela expansão do nó atual.
        """
        sucessores = []
        if no.profundidade < self._prof_max:
            estado = no.estado
            for operador in problema.operadores:
                estado_suc = operador.aplicar(estado)
                if estado_suc is not None:
                    custo = no.custo + operador.custo(estado, estado_suc)
                    no_successor = No(estado_suc, operador, no, custo)
                    sucessores.append(no_successor)
        return sucessores
