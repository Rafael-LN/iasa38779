from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    def prioridade(self, no):
        return no.custo
