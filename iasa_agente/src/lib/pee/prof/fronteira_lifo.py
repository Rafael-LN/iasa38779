from pee.mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    def inserir(self, no):
        self._nos.append(no)