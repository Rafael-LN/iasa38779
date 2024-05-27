from pdm.pdm import PDM
from plan.plan_pdm.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

class PlaneadorPDM(Planeador):
    """
    A classe PlaneadorPDM estende a classe Planeador e implementa um planeador baseado em Processos de Decisão de Markov (PDM).

    Atributos:
        __gama (float): Fator de desconto para recompensas diferidas.
        __delta_max (float): Critério de convergência para a diferença máxima na atualização das utilidades.

    Métodos:
        __init__(self, gama=0.85, delta_max=1): Inicializa a instância da classe com os parâmetros fornecidos.
        planear(self, modelo_plan, objetivos): Gera um plano baseado em PDM para os objetivos fornecidos.
    """

    def __init__(self, gama=0.85, delta_max=1):
        """
        Inicializa uma instância da classe PlaneadorPDM.

        Parâmetros:
            gama (float, opcional): Fator de desconto para recompensas diferidas, com valor padrão de 0.85.
            delta_max (float, opcional): Critério de convergência para a diferença máxima na atualização das utilidades, com valor padrão de 1.

        Este método inicializa os atributos gama e delta_max com os valores fornecidos ou os valores padrão.
        """
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objetivos):
        """
        Gera um plano baseado em PDM para os objetivos fornecidos.

        Este método cria uma instância de ModeloPDMPlan com o modelo de planeamento e os objetivos, resolve o PDM utilizando a classe PDM, e retorna um plano com as utilidades e políticas calculadas.

        Parâmetros:
            modelo_plan: Instância do modelo de planeamento que define os estados e ações.
            objetivos: Lista de estados objetivo a serem alcançados.

        Retorna:
            PlanoPDM: Um plano contendo as utilidades dos estados e a política ótima para alcançar os objetivos.
        """
        modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
        U, P = pdm.resolver()

        return PlanoPDM(U, P)
