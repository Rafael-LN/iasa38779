from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    """
    Classe que representa um passo na solução de um problema de procura.
    Contém um estado e o operador que levou a esse estado.
    """

    estado: Estado
    operador: Operador
    """
    Atributos:
    estado: O estado alcançado neste passo da solução.
    operador: O operador aplicado para alcançar este estado.
    """
