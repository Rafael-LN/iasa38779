from controlo_react.reaccoes.evitar.estimuloObst import EstimuloObst
from ecr.reaccao import Reaccao


class EvitarDir(Reaccao):
    """
    Classe que representa uma reação para evitar uma direção específica.
    Herda da classe Reaccao.
    """
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)