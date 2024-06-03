from pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof, limite_prof):
        super().prof_max
        for i in range(0, limite_prof, inc_prof):
            solucao = super.procurar(problema)
            if solucao:
                return solucao
        return solucao