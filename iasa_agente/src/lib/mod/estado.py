from abc import ABC, abstractmethod

class Estado(ABC):
    """
    Classe abstrata que define um estado do problema.

    Métodos Abstratos:
        id_valor(): Método abstrato que retorna um identificador único para o estado.

    Métodos Especiais:
        __eq__(outro): Método especial que verifica se dois estados são iguais.
        __hash__(): Método especial que retorna o hash do estado.

    Nota:
        Esta classe deve ser subclassificada e o método abstrato `id_valor` deve ser implementado.
    """

    @abstractmethod
    def id_valor(self):
        """
        Retorna um identificador único para o estado.

        Returns:
            Um identificador único para o estado.
        """
        pass

    def __eq__(self, outro):
        """
        Verifica se dois estados são iguais.

        Args:
            outro: O outro estado a ser comparado.

        Returns:
            True se os estados forem iguais, False caso contrário.
        """
        return isinstance(outro, Estado) and self.id_valor() == outro.id_valor()

    def __hash__(self):
        """
        Retorna o hash do estado.

        Returns:
            O hash do estado.
        """
        return hash(self.id_valor())
