from mod.problema import Problema


class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estados().pop(0), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    def objectivo(self, estado):
        return estado == self.__estado_final