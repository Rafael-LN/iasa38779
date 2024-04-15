from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao():
    """
    Classe que representa um passo de uma solução, contendo um estado e o operador que levou a esse estado.

    Attributes:
        estado (Estado): O estado associado a este passo da solução.
        operador (Operador): O operador que foi aplicado para chegar a este estado.
    """
    estado: Estado
    operador: Operador