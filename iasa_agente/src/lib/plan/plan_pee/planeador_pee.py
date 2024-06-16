from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

class PlaneadorPEE(Planeador):
    """
    A classe PlaneadorPEE implementa um planeador que utiliza o algoritmo de procura em espaço de estados A* (ProcuraMelhorPrim) para planear trajetórias. Este planeador é projetado para gerar planos de ação para um agente com base em um modelo de planeamento e uma lista de objetivos.

    Atributos:
        __mec_pee (ProcuraMelhorPrim): Instância do mecanismo de procura A* utilizada para resolver o problema de planeamento.
    """

    def __init__(self):
        """
        Método construtor da classe PlaneadorPEE.

        Inicializa o planeador configurando o mecanismo de procura (__mec_pee) como None. A configuração do mecanismo de procura é feita no método planear.

        Parâmetros:
            Nenhum.
        """
        self.__mec_pee = None
        
    def planear(self, modelo_plan, objectivos):
        """
        Método que gera um plano de ação para um agente com base em um modelo de planeamento e uma lista de objetivos.

        Este método utiliza o algoritmo de procura A* (ProcuraMelhorPrim) para resolver o problema de planeamento definido pelo modelo de planeamento e o estado objetivo. A heurística utilizada é a distância euclidiana (HeurDist) até o estado objetivo. A solução encontrada é convertida em um plano de ação (PlanoPEE).

        Parâmetros:
            modelo_plan: Instância do modelo de planeamento que define os estados e operadores.
            objectivos (list): Lista de estados objetivo a serem alcançados.

        Retorna:
            PlanoPEE: Instância do plano de ação contendo a solução encontrada.
        """
       
        
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            self.__mec_pee = ProcuraMelhorPrim(heuristica)
            solucao = self.__mec_pee.procurar(problema, heuristica)

            if solucao:
                return PlanoPEE(solucao)
            else:
                return None
