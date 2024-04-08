from ecr.comportamento import Comportamento
from sae.agente.percepcao import Percepcao

class Reaccao(Comportamento):
    """
    Classe que representa uma reação a um estímulo, derivada da classe Comportamento.
    """

    def __init__(self, estimulo, resposta):
        """
        Método construtor da classe Reaccao.

        :param estimulo: Estímulo ao qual a reação está associada.
        :param resposta: Resposta que será ativada quando o estímulo for detetado.
        """
        self.estimulo = estimulo
        self.resposta = resposta
        
    def activar(self, percepcao):
        """
        Ativa a reação com base numa perceção.

        :param percepcao: Perceção que desencadeia a reação.
        :return: Ação associada à resposta se o estímulo for detetado com intensidade positiva.
        """
        intensidade = self.estimulo.detectar(percepcao)
        
        if intensidade > 0:
            return self.resposta.activar(percepcao, intensidade)

                