from pee.mec_proc.mecanismoProcura import MecanismoProcura

class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        super().__init__()
        self.__nos_mem_max = 0
        
    def _memorizar(self, no):
        
        if self.dimensao > self.__nos_mem_max:
            self.__nos_mem_max = self.dimensao
        
    def nos_memoria(self):
         return self.__nos_mem_max