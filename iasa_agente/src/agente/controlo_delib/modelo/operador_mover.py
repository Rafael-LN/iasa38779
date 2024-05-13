class OperadorMover():
    def __init__(self, modelo_mundo, direccao):
        """
        Inicializa o operador de mover com o modelo do mundo e a direção especificada.

        Argumentos:
            modelo_mundo: O modelo do mundo onde o operador será aplicado.
            direccao: A direção na qual o operador moverá o agente.
        """
        self.__modelo_mundo = modelo_mundo
        
    @property
    def ang(self):
        """
        Obtém o ângulo do operador de mover.

        Retorno:
            O ângulo do operador de mover.
        """
        return self.ang

    @property
    def accao(self):
        """
        Obtém a ação associada ao operador de mover.

        Retorno:
            A ação associada ao operador de mover.
        """
        return self.accao
    
    def aplicar(self, estado):
        """
        Aplica o operador de mover ao estado especificado.

        Argumentos:
            estado: O estado ao qual aplicar o operador de mover.

        Retorno:
            O novo estado resultante da aplicação do operador de mover.
        """
        # FAZER:
        # fazer a translação para obter nova posicao
        # criar um estado agente para a nova posicao
        # -> Validar se os estado é valido:
        #   Se esse estado for um estado do modelo do mundo
        #   então retorna esse estado
        pass
    
    def custo(self, estado, estado_suc):
        """
        Calcula o custo de aplicar o operador de mover do estado inicial ao estado sucessor.

        Argumentos:
            estado: O estado inicial.
            estado_suc: O estado sucessor.

        Retorno:
            O custo de aplicar o operador de mover do estado inicial ao estado sucessor.
        """
        # return double
        pass
    
    def __translacao(self, posicao, distancia, angulo):
        """
        Realiza uma translação da posição especificada.

        Argumentos:
            posicao: A posição inicial.
            distancia: A distância da translação.
            angulo: O ângulo da translação.

        Retorno:
            A nova posição resultante da translação.
        """
        # return Posicao
        pass
