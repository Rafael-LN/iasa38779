from controlo_react.reaccoes.aproximar.aproximarAlvo import AproximarAlvo
from controlo_react.reaccoes.resposta.respostaMover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    """
    Classe que representa uma reação para aproximar o agente numa direção específica.
    Herda da classe Reaccao.
    """
    def __init__(self, direccao):
        super(AproximarAlvo(direccao), RespostaMover(direccao))