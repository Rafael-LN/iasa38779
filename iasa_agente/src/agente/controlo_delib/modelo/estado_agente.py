from mod.estado import Estado

class EstadoAgente(Estado):
    """
    Classe que representa o estado de um agente num espaço de estados.
    Herda da classe Estado e define a posição do agente como o estado.
    """

    def __init__(self, posicao):
        """
        Inicializa uma nova instância de EstadoAgente.

        Parâmetros:
        posicao: A posição do agente que define o estado.

        Funcionalidade:
        Este construtor inicializa a posição do agente.
        """
        self.__posicao = posicao

    @property
    def posicao(self):
        """
        Obtém a posição do agente.

        Retorna:
        A posição do agente.

        Funcionalidade:
        Este método retorna a posição atual do agente.
        """
        return self.__posicao
    
    def id_posicao(self):
        """
        Obtém o identificador da posição do agente.

        Retorna:
        O identificador da posição do agente.

        Funcionalidade:
        Este método retorna o valor único que identifica a posição do agente.
        """
        return self.__id_valor
    
    def id_valor(self):
        """
        Retorna um valor que identifica unicamente o estado.

        Retorna:
        Um valor de hash que representa o estado.

        Funcionalidade:
        Este método retorna o valor de hash da posição do agente, fornecendo uma representação única do estado.
        """
        return hash(self.__posicao)
