from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Classe abstrata que define um operador para manipulação de estados.

    Métodos Abstratos:
        aplicar(estado): Método abstrato para aplicar o operador a um estado e retornar o novo estado resultante.
        custo(estado, estado_suc): Método abstrato para calcular o custo do operador ao transitar de um estado para outro.

    Nota:
        Esta classe deve ser subclassificada e os métodos abstratos devem ser implementados.
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Aplica o operador a um estado e retorna o novo estado resultante.

        Args:
            estado: O estado atual.

        Returns:
            O novo estado resultante após a aplicação do operador.
        """
        pass
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Calcula o custo do operador ao transitar de um estado para outro.

        Args:
            estado: O estado atual.
            estado_suc: O estado sucessor após a aplicação do operador.

        Returns:
            O custo associado ao operador ao transitar de um estado para outro.
        """
        pass
