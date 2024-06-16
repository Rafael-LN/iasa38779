from plan.plano import Plano

class PlanoPDM(Plano):
    """
    Classe que implementa um plano baseado em Processos de Decisão Markovianos (PDM).
    Herda da classe Plano e armazena a utilidade dos estados e a política de ações.
    """

    def __init__(self, utilidade, politica):
        """
        Inicializa uma nova instância de PlanoPDM.

        Parâmetros:
        utilidade: Um dicionário contendo a utilidade de cada estado.
        politica: Um dicionário contendo a ação ótima para cada estado.

        Funcionalidade:
        Este construtor inicializa a utilidade dos estados e a política de ações com os valores fornecidos.
        """
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """
        Obtém a ação a ser executada para um dado estado com base na política.

        Parâmetros:
        estado: O estado para o qual se pretende obter a ação.

        Retorna:
        A ação ótima para o estado fornecido, ou None se o estado não estiver na política.

        Funcionalidade:
        Este método retorna a ação ótima associada ao estado fornecido de acordo com a política calculada.
        Verifica se o estado está presente na política antes de retornar a ação.
        """
        if estado and estado in self.__politica:
            return self.__politica[estado]

    def mostrar(self, vista):
        """
        Mostra a visualização do plano utilizando uma vista fornecida.

        Parâmetros:
        vista: Objeto responsável por exibir a visualização do plano.

        Funcionalidade:
        Este método utiliza a vista para mostrar a utilidade dos estados e a direção das ações associadas.
        Para cada estado, exibe o valor da utilidade e a ação ótima.
        """
        if self.__politica:
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
        
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
