from pdm.mec_util import MecUtil


class PDM():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):
        pass
    
    def resolver(self):
        pass