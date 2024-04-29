from abc import ABC, abstractmethod

class Problema(ABC):
    """
    Classe abstrata que define um problema a ser resolvido.

    Atributos:
        estado_inicial: O estado inicial do problema.
        operadores: Uma lista de operadores disponíveis para resolver o problema.

    Métodos Abstratos:
        objectivo(estado): Método abstrato que verifica se um determinado estado atinge o objetivo do problema.
    """

    def __init__(self, estado_inicial, operadores):
        """
        Inicializa o problema com o estado inicial e a lista de operadores disponíveis.

        Args:
            estado_inicial: O estado inicial do problema.
            operadores: Uma lista de operadores disponíveis para resolver o problema.
        """
        self.estado_inicial = estado_inicial
        self.operadores = operadores
        
    @abstractmethod
    def objectivo(self, estado):
        """
        Verifica se um determinado estado atinge o objetivo do problema.

        Args:
            estado: O estado a ser verificado.

        Retorno:
            True se o estado atinge o objetivo do problema, False caso contrário.
        """
        pass
