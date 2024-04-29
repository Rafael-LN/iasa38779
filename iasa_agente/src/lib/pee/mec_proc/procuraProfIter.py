from pee.mec_proc.procuraProfLim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    def procurar(self, problema, inc_prof, limite_prof):
        for i in range(0, limite_prof, inc_prof):
            pass