from mod.problema import Problema


class ProblemaPan(Problema):
    def __init__(self, modelo_plan, estado_final):
        self.__estado_final = estado_final
        
    def objectivo(self, estado):
        return super().objectivo(estado)