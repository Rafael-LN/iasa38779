from ecr.resposta import Resposta
from sae.agente.accao import Accao


class RespostaMover(Resposta):
    """
    Classe que representa uma resposta para mover um agente em uma determinada direção.
    Herda da classe Resposta.
    """

    def __init__(self, direccao):
        """
        Método construtor da classe RespostaMover.
        
        Args:
            direccao: Direção para onde o agente se deve mover.
        """
        super().__init__(Accao(direccao)) # Inicializa a classe pai (Resposta) com uma ação (Accao) na direção especificada.