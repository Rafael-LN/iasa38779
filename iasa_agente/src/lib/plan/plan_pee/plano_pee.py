from plan.plano import Plano

class PlanoPEE(Plano):
    """
    A classe PlanoPEE representa um plano baseado em uma sequência de passos (solução) gerados por um algoritmo de planeamento.

    Atributos:
        __passos (list): Lista de passos que compõem a solução do plano.

    Métodos:
        __init__(self, solucao): Inicializa a instância da classe com a solução fornecida.
        obter_accao(self, estado): Retorna a ação a ser tomada para um determinado estado, removendo o passo correspondente da lista.
        mostrar(self, vista): Exibe os passos do plano como vetores em uma determinada visão.
    """

    def __init__(self, solucao):
        """
        Inicializa uma instância da classe PlanoPEE.

        Parâmetros:
            solucao (list): Lista de passos que compõem a solução do plano.

        Este método inicializa o atributo __passos com os passos fornecidos na solução.
        """
        self.__passos = [passo for passo in solucao]
        
    def obter_accao(self, estado):
        """
        Retorna a ação a ser tomada para um determinado estado.

        Parâmetros:
            estado: O estado atual para o qual se deseja obter a ação.

        Retorna:
            Operador correspondente ao estado atual, removido da lista de passos.
        """
        for passo in self.__passos:
            if passo.estado == estado:
                return passo.operador
        return None
    
    def validar_estado(self, estado):
        """
        Valida se um estado está presente no plano.

        Args:
            estado (Estado): O estado a ser validado.

        Retorna:
            bool: True se o estado está presente no plano, False caso contrário.
        """
        for passo in self.__passos:
            if passo.estado == estado:
                return True
        return False
    
    def mostrar(self, vista):
        """
        Exibe os passos do plano como vetores em uma determinada visão.

        Parâmetros:
            vista: A visão ou contexto em que o plano deve ser apresentado.

        Este método utiliza a visão fornecida para exibir os vetores dos passos do plano.
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
