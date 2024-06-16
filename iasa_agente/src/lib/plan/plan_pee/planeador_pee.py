from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

class PlaneadorPEE(Planeador):
    """
    Classe que implementa um planeador automático baseado no método PEE (Procura em Espaços de Estados).
    Herda da classe Planeador e utiliza métodos de procura heurística para gerar planos de ação a partir de objetivos definidos.
    """

    def __init__(self):
        """
        Inicializa uma nova instância do PlaneadorPEE.
        
        Atributos:
        __mec_pee: Armazena o mecanismo de procura utilizado no planeamento. Inicialmente definido como None.
        
        Funcionalidade:
        Este construtor inicializa o atributo __mec_pee como None, indicando que nenhum mecanismo de procura foi configurado ainda.
        """
        self.__mec_pee = None

    def planear(self, modelo_plan, objectivos):
        """
        Gera um plano de ação a partir de um modelo de planeamento e uma lista de objetivos.

        Parâmetros:
        modelo_plan: Representa o modelo do mundo sobre o qual o planeamento será realizado.
        objectivos: Lista de objetivos que o agente deve alcançar. Assume-se que a lista contém pelo menos um objetivo.

        Retorna:
        Um objeto PlanoPEE que representa o plano de ações gerado para alcançar o objetivo, ou None se não for possível encontrar uma solução.

        Funcionalidade:
        1. Verifica se a lista de objetivos não está vazia.
        2. Extrai o primeiro objetivo como estado final desejado.
        3. Cria uma instância de ProblemaPlan com base no modelo de planeamento e no estado final.
        4. Cria uma heurística (HeurDist) com base no estado final para guiar a procura.
        5. Inicializa o mecanismo de procura ProcuraMelhorPrim com a heurística criada.
        6. Realiza a procura da solução utilizando o mecanismo de procura e a heurística.
        7. Se uma solução for encontrada, retorna um PlanoPEE com a sequência de ações; caso contrário, retorna None.
        """
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            self.__mec_pee = ProcuraMelhorPrim(AvaliadorCustoUnif())
            solucao = self.__mec_pee.procurar(problema)

            if solucao:
                return PlanoPEE(solucao)
            else:
                return None
