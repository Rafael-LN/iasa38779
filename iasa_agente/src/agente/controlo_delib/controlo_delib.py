from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae.agente.controlo import Controlo

class ControloDelib(Controlo):
    """
    Classe para implementar o controlo deliberativo de um agente.

    Atributos:
        __objectivos (list): Lista de objetivos do agente.
        __mec_delib (objeto): Mecanismo de deliberação do agente.
        __planeador (objeto): Planeador utilizado para gerar planos de ação.
        __plano (objeto): Plano de ação gerado pelo planeador.
        __modelo_mundo (objeto): Modelo do mundo do agente.

    Métodos:
        __init__: Inicializa o controlo deliberativo com o planeador especificado.
        processar: Processa a percepção atual e decide qual ação o agente deve executar.
        __mostrar: Atualiza a visualização do ambiente para refletir o estado atual do agente e do mundo.
        __assimilar: Assimila a percepção atual para atualizar o modelo do mundo do agente.
        __reconsiderar: Verifica se o agente deve reconsiderar a sua estratégia de ação.
        __deliberar: Delibera sobre os objetivos do agente e decide o que deve fazer em seguida.
        __planear: Planeia uma sequência de ações para alcançar os objetivos do agente.
        __executar: Executa a próxima ação do plano de ação gerado.
    """

    def __init__(self, planeador):
        """
        Inicializa o controlo deliberativo com o planeador especificado.

        Argumentos:
            planeador: O planeador a ser utilizado para deliberar e planear a ação do agente.
        """
        self.__objectivos = []  # Lista de objetivos do agente
        self.__planeador = planeador  # Planeador utilizado para gerar planos de ação
        self.__modelo_mundo = ModeloMundo()  # Modelo do mundo do agente
        self.__mec_delib = MecDelib(self.__modelo_mundo)  # Mecanismo de deliberação do agente
        self.__plano = None  # Plano de ação gerado pelo planeador
        
    def processar(self, percepcao):
        """
        Processa a percepção atual e decide qual ação o agente deve executar.

        Argumentos:
            percepcao: A percepção atual do agente.

        Retorno:
            A ação a ser executada pelo agente.
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()
    
    def __assimilar(self, percepcao):
        """
        Assimila a percepção atual para atualizar o modelo do mundo do agente.

        Argumentos:
            percepcao: A percepção atual do agente.
        """
        self.__modelo_mundo.actualizar(percepcao)
        
    def __reconsiderar(self):
        """
        Verifica se o agente deve reconsiderar a sua estratégia de ação.

        Retorno:
            True se o agente deve reconsiderar, False caso contrário.
        """
        if self.__modelo_mundo.alterado or self.__plano == None:
            return True
        return False
    
    def __deliberar(self):
        """
        Delibera sobre os objetivos do agente e decide o que deve fazer em seguida.
        """
        self.__objectivos = self.__mec_delib.deliberar()
    
    def __planear(self):
        """
        Planeia uma sequência de ações para alcançar os objetivos do agente.
        """
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        
    
    def __executar(self):
        """
        Executa a próxima ação do plano de ação gerado.
        
        Retorno:
            A próxima ação a ser executada pelo agente.
        """
        if self.__plano:

            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())

            if operador:
                return operador.accao
    
    def __mostrar(self):
        """
        Atualiza a visualização do ambiente para refletir o estado atual do agente e do mundo.
        """
        self.vista.limpar()  # Limpa a vista do ambiente
        self.__modelo_mundo.mostrar(self.vista)  # Mostra o modelo do mundo no ambiente
        
        if self.__plano:
            self.__plano.mostrar(self.vista)  # Mostra o plano de ação no ambiente
        
        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo)  # Marca os objetivos no ambiente
