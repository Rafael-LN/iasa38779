from pdm.pdm import PDM
from plan.plan_pdm.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

class PlaneadorPDM(Planeador):
    """
    Classe que implementa um planeador baseado em Processos de Decisão Markovianos (PDM).
    Herda da classe Planeador e utiliza um PDM para gerar planos de ação que maximizam a utilidade dos estados.
    """

    def __init__(self, gama=0.85, delta_max=1):
        """
        Inicializa uma nova instância de PlaneadorPDM.

        Parâmetros:
        gama: O fator de desconto utilizado no cálculo da utilidade.
        delta_max: O valor máximo de variação (delta) para o critério de convergência.

        Funcionalidade:
        Este construtor inicializa os parâmetros gama e delta_max para o cálculo da utilidade no PDM.
        """
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objetivos):
        """
        Gera um plano de ações para alcançar os objetivos a partir do modelo de planeamento utilizando um PDM.

        Parâmetros:
        modelo_plan: O modelo de planeamento que define os estados e operadores.
        objetivos: A lista de objetivos que se pretende alcançar.

        Retorna:
        Um plano de ações representado pela classe PlanoPDM.

        Funcionalidade:
        Este método cria um ModeloPDMPlan com base no modelo de planeamento e nos objetivos fornecidos,
        resolve o PDM para calcular a utilidade dos estados e a política ótima, e retorna um plano de ações que maximiza a utilidade.
        """
        modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
        U, P = pdm.resolver()

        return PlanoPDM(U, P)
