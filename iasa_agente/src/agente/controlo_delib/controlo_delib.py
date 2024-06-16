from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae.agente.controlo import Controlo

class ControloDelib(Controlo):
    """
    Classe que implementa o controlo deliberativo de um agente.
    Herda da classe Controlo e utiliza um planeador para gerar planos de ação com base em objetivos e perceções do ambiente.
    """

    def __init__(self, planeador):
        """
        Inicializa uma nova instância de ControloDelib.

        Parâmetros:
        planeador: O planeador utilizado para gerar planos de ação.

        Funcionalidade:
        Este construtor inicializa os atributos do agente, incluindo a lista de objetivos, o modelo do mundo, o mecanismo de deliberação e o plano de ação.
        """
        self.__objectivos = []  # Lista de objetivos do agente
        self.__planeador = planeador  # Planeador utilizado para gerar planos de ação
        self.__modelo_mundo = ModeloMundo()  # Modelo do mundo do agente
        self.__mec_delib = MecDelib(self.__modelo_mundo)  # Mecanismo de deliberação do agente
        self.__plano = None  # Plano de ação gerado pelo planeador

    def processar(self, percepcao):
        """
        Processa uma nova perceção do ambiente e atualiza o estado do agente.

        Parâmetros:
        percepcao: A perceção recebida do ambiente.

        Retorna:
        A ação a ser executada pelo agente com base na perceção processada.

        Funcionalidade:
        Este método segue um ciclo de processamento que inclui assimilação da perceção, reconsideração do estado atual,
        deliberação de novos objetivos, planeamento de ações e execução do plano gerado.
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    def __assimilar(self, percepcao):
        """
        Atualiza o modelo do mundo com a nova perceção.

        Parâmetros:
        percepcao: A perceção recebida do ambiente.

        Funcionalidade:
        Este método atualiza o modelo do mundo com as informações da perceção recebida.
        """
        self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        """
        Verifica se é necessário reconsiderar os objetivos ou o plano atual.

        Retorna:
        True se o modelo do mundo foi alterado ou se não há um plano atual, False caso contrário.

        Funcionalidade:
        Este método determina se há necessidade de reconsiderar os objetivos ou o plano, com base nas alterações no modelo do mundo ou na ausência de um plano.
        """
        return self.__modelo_mundo.alterado or self.__plano is None

    def __deliberar(self):
        """
        Delibera novos objetivos para o agente.

        Funcionalidade:
        Este método utiliza o mecanismo de deliberação para definir novos objetivos com base no estado atual do modelo do mundo.
        """
        self.__objectivos = self.__mec_delib.deliberar()

    def __planear(self):
        """
        Gera um novo plano de ação com base nos objetivos e no modelo do mundo.

        Funcionalidade:
        Este método utiliza o planeador para gerar um plano de ação que permita ao agente alcançar os objetivos definidos.
        """
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)

    def __executar(self):
        """
        Executa a próxima ação do plano de ação.

        Retorna:
        A ação a ser executada pelo agente.

        Funcionalidade:
        Este método obtém a próxima ação do plano de ação com base no estado atual do modelo do mundo e retorna essa ação para execução.
        Se não houver um operador disponível, retorna None.
        """
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao

    def __mostrar(self):
        """
        Mostra a visualização do modelo do mundo, do plano de ação e dos objetivos.

        Funcionalidade:
        Este método utiliza a vista para limpar a visualização atual e mostrar o modelo do mundo, o plano de ação e os objetivos no ambiente.
        """
        self.vista.limpar()  # Limpa a vista do ambiente
        self.__modelo_mundo.mostrar(self.vista)  # Mostra o modelo do mundo no ambiente

        if self.__plano:
            self.__plano.mostrar(self.vista)  # Mostra o plano de ação no ambiente

        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo)  # Marca os objetivos no ambiente
