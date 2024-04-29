from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no):
        return no.custo
