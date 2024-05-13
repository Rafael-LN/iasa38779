from agente.controlo_delib.modelo.estado_agente import EstadoAgente


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
            O novo estado resultante da aplicação do operador de mover, se válido; caso contrário, None.
        """
        # Fazer a translação para obter a nova posição
        nova_posicao = self.__translacao(estado.posicao, distancia=1, angulo=self.__direccao)
    
        # Criar um estado agente para a nova posição
        novo_estado = EstadoAgente(nova_posicao)  # Supondo que haja uma classe Estado que represente o estado do agente
    
        # Validar se o estado é válido:
        if novo_estado in self.__modelo_mundo.obter_estados():
            # Se esse estado for um estado do modelo do mundo, então retorna esse estado
            return novo_estado
        else:
            # Caso contrário, retorna None
            return None

    
    def custo(self, estado, estado_suc):
        """
        Calcula o custo de aplicar o operador de mover do estado inicial ao estado sucessor.

        Argumentos:
            estado: O estado inicial.
            estado_suc: O estado sucessor.

        Retorno:
            O custo de aplicar o operador de mover do estado inicial ao estado sucessor.
        """
        return self.__modelo_mundo.distancia(estado_suc)
    
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
