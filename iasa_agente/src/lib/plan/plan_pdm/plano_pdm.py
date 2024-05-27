from plan.plano import Plano

class PlanoPDM(Plano):
    """
    A classe PlanoPDM representa um plano baseado em Processos de Decisão de Markov (PDM), contendo utilidades dos estados e a política ótima.

    Atributos:
        __utilidade (dict): Dicionário que mapeia estados às suas respectivas utilidades.
        __politica (dict): Dicionário que mapeia estados às ações ótimas a serem tomadas.

    Métodos:
        __init__(self, utilidade, politica): Inicializa a instância da classe com as utilidades dos estados e a política ótima.
        obter_accao(self, estado): Retorna a ação ótima a ser tomada para um determinado estado.
        mostrar(self, vista): Exibe as utilidades dos estados e as ações da política ótima em uma determinada visão.
    """

    def __init__(self, utilidade, politica):
        """
        Inicializa uma instância da classe PlanoPDM.

        Parâmetros:
            utilidade (dict): Dicionário que mapeia estados às suas respectivas utilidades.
            politica (dict): Dicionário que mapeia estados às ações ótimas a serem tomadas.

        Este método inicializa os atributos utilidade e politica com os valores fornecidos.
        """
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """
        Retorna a ação ótima a ser tomada para um determinado estado.

        Parâmetros:
            estado: O estado para o qual se deseja obter a ação.

        Retorna:
            Ação ótima a ser tomada no estado fornecido, ou None se o estado não estiver na política definida.
        """
        if estado and estado in self.__politica:
            return self.__politica[estado]

    def mostrar(self, vista):
        """
        Exibe as utilidades dos estados e as ações da política ótima em uma determinada visão.

        Parâmetros:
            vista: A visão ou contexto em que o plano deve ser apresentado.

        Este método utiliza a visão fornecida para exibir os valores de utilidade e as direções das ações ótimas para cada estado.
        """
        if self.__politica:
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
        
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
