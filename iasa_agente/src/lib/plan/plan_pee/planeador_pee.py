from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador


class PlaneadorPEE(Planeador):
    def __init__(self):
        self.__mec_pee
        
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            estado_final = objectivos.pop(0)
            problema = ProblemaPlan(modelo_plan, estado_final)
            self.__mec_pee = ProcuraAA()
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_pee.resolver(problema, heuristica)

            return PlanoPEE(solucao)
    