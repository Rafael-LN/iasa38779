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
        self.__mec_delib = None  # Mecanismo de deliberação do agente
        self.__planeador = planeador  # Planeador utilizado para gerar planos de ação
        self.__plano = None  # Plano de ação gerado pelo planeador
        self.__modelo_mundo = None  # Modelo do mundo do agente
        
    def processar(self, percepcao):
        """
        Processa a percepção atual e decide qual ação o agente deve executar.

        Argumentos:
            percepcao: A percepção atual do agente.

        Retorno:
            A ação a ser executada pelo agente.
        """
        #Return accao
        pass
    
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
        return self.__modelo_mundo.alterado
    
    def __deliberar(self):
        """
        Delibera sobre os objetivos do agente e decide o que deve fazer em seguida.
        """
        self.__mec_delib.deliberar()
    
    def __planear(self):
        """
        Planeia uma sequência de ações para alcançar os objetivos do agente.
        """
        # Se não houver objectivos colocar o plano a None
        if len(self.__objectivos) == 0:
            self.__plano = None
        
    
    def __executar(self):
        """
        Executa a próxima ação do plano de ação gerado.
        
        Retorno:
            A próxima ação a ser executada pelo agente.
        """
        #return Accao
        pass
    
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
