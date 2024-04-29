from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao


class EvitarObst(Hierarquia):
    """
    Classe que representa um comportamento para evitar obstáculos organizados de forma hierárquica.
    Herda da classe Hierarquia.
    """
    def __init__(self):
        super().__init__([EvitarDir(direccao, RespostaEvitar(direccao)) for direccao in Direccao])