from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    A classe ProblemaPlan estende a classe Problema e representa um problema de planeamento que utiliza um modelo de planeamento e define um estado final objetivo.

    Atributos:
        __estado_final: Estado que representa o objetivo final do problema.

    Métodos:
        __init__(self, modelo_plan, estado_final): Inicializa a instância da classe com o modelo de planeamento e o estado final objetivo.
        objectivo(self, estado): Verifica se um estado é o estado final objetivo.
    """

    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa uma instância da classe ProblemaPlan.

        Parâmetros:
            modelo_plan: Instância do modelo de planeamento que define os estados e operadores.
            estado_final: Estado que representa o objetivo final do problema.

        Este método inicializa a classe base Problema com o estado inicial (o primeiro estado do conjunto de estados) e os operadores do modelo de planeamento.
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    def objectivo(self, estado):
        """
        Verifica se um estado é o estado final objetivo.

        Parâmetros:
            estado: O estado a ser verificado.

        Retorna:
            bool: True se o estado for o estado final objetivo, caso contrário, False.
        """
        return estado.posicao == self.__estado_final.posicao
