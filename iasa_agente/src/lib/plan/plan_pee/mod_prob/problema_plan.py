from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Classe que define um problema de planeamento para sistemas autónomos.

    Esta classe estende a classe abstrata Problema e é projetada para representar um problema específico de planeamento
    para um sistema autónomo.

    Atributos:
        estado_inicial: O estado inicial do problema de planeamento.
        operadores: Uma lista de operadores disponíveis para resolver o problema.
        estado_final: O estado final desejado que indica a condição de sucesso do problema.

    Métodos:
        __init__: Inicializa o problema de planeamento com o estado inicial, operadores e estado final.
        objectivo: Verifica se um estado atinge o objetivo do problema de planeamento.
    """

    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa um problema de planeamento com o modelo de planeamento, estado final e operadores.

        Args:
            modelo_plan: O modelo de planeamento utilizado para o problema.
            estado_final: O estado final desejado que indica a condição de sucesso do problema.
        """
        super().__init__(modelo_plan.obter_estados().pop(0), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    def objectivo(self, estado):
        """
        Verifica se um determinado estado atinge o objetivo do problema de planeamento.

        Args:
            estado: O estado a ser verificado.

        Returns:
            True se o estado atinge o objetivo do problema de planeamento, False caso contrário.
        """
        return estado == self.__estado_final
