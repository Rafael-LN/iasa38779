from mod.estado import Estado

class EstadoAgente(Estado):
    def __init__(self, posicao):
        """
        Inicializa um estado do agente com a posição especificada.

        Argumentos:
            posicao: A posição do agente no ambiente.
        """
        self.__posicao = posicao
        
    @property
    def posicao(self):
        """
        Retorna a posição do agente.

        Retorno:
            A posição do agente.
        """
        return self.__posicao
    
    def id_posicao(self):
        """
        Retorna o identificador da posição do agente.

        Este método é necessário para fins de comparação ou identificação de posições.

        Retorno:
            O identificador da posição do agente.
        """
        pass
