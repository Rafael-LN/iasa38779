from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorHeur(Avaliador):
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica