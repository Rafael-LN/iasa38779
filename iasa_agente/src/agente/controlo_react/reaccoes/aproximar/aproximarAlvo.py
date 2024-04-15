from controlo_react.reaccoes.aproximar.aproximarDir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao


class AproximarAlvo(Prioridade):
    """
    Classe que representa um conjunto de comportamentos de aproximação a um alvo consoante organizados por prioridade.
    Herda da classe Prioridade.
    """

    def __init__(self):
        
        super().__init__([AproximarDir(direction) for direction in Direccao])  # Inicializa a classe pai (Prioridade) com a lista de comportamentos fornecida.