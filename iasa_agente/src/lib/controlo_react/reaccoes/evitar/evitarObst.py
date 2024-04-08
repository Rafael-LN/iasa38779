from controlo_react.reaccoes.evitar.evitarDir import EvitarDir
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


class EvitarObst(Hierarquia):
    """
    Classe que representa um comportamento para evitar obstáculos organizados de forma hierárquica.
    Herda da classe Hierarquia.
    """
    def __init__(self):
        super().__init__([EvitarDir(direction) for direction in Direccao])