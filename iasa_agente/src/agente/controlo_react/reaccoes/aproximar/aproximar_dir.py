from controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    """
    Classe que representa uma reação para aproximar o agente numa direção específica.
    Herda da classe Reaccao.
    """
    def __init__(self, direccao):
        """
        Método construtor da classe AproximarDir.
        
        Args:
            direccao (int): Direção para a qual o agente deve se aproximar.
        """
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
        # Inicializa a classe pai (Reaccao) com um estímulo associado à direção especificada e uma resposta para mover na mesma direção.