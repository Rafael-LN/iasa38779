from pee.larg.procura_grafo import ProcuraGrafo


class ProcuraMelhorPrim(ProcuraGrafo):
    def __init__(self, avaliador):
        self._avaliador = avaliador
        
    def _manter(self, no):
        return super()._manter(no)