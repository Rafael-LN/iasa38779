from sae import Accao


class Resposta(Accao):
    """
        Classe que representa uma resposta a uma perceção,
        derivada da classe Accao.
    """
    
    def __init__(self, accao):
        """
            Método construtor da classe Resposta.
            :param accao: Ação associada à resposta.
        """
        self._accao = accao
        
    def activar(self, percepcao, intensidade=0.0):
        
        """
        Ativa a resposta se uma percepção for verdadeira.
        :param percepcao: A percepção que desencadeia a resposta.
        :param intensidade: A intensidade da resposta (opcional).
        :return: A ação associada à resposta se a percepção for verdadeira, caso contrário, None.
        """
        if percepcao:
            self._accao.prioridade = intensidade
            return self._accao
