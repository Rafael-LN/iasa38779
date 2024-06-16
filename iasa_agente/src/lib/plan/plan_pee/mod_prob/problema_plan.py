from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Classe que representa um problema de planeamento específico para o contexto de PEE (Procura em Espaços de Estados).
    Herda da classe Problema e define o estado inicial, os operadores e o estado objetivo para a resolução do problema.
    """

    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa uma nova instância de ProblemaPlan com base no modelo de planeamento e no estado final desejado.

        Parâmetros:
        modelo_plan: O modelo de planeamento que fornece o estado inicial e os operadores para o problema.
        estado_final: O estado objetivo que se pretende alcançar.

        Funcionalidade:
        Este construtor chama o construtor da classe base Problema para inicializar o estado inicial e os operadores utilizando o modelo de planeamento fornecido.
        Adicionalmente, armazena o estado final que será usado para determinar se um estado é objetivo.
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    def objectivo(self, estado):
        """
        Verifica se um determinado estado é o estado objetivo.

        Parâmetros:
        estado: O estado que se pretende verificar.

        Retorna:
        True se a posição do estado fornecido for igual à posição do estado final, False caso contrário.

        Funcionalidade:
        Este método compara a posição do estado atual com a posição do estado final armazenado.
        Se as posições coincidirem, o estado é considerado objetivo e o método retorna True; caso contrário, retorna False.
        """
        return estado.posicao == self.__estado_final.posicao
