from abc import ABC, abstractmethod


class Comportamento(ABC):
    """
    Classe abstrata que representa um comportamento.
    """

    @abstractmethod
    def activar(self, percepcao):
        """
        Método abstrato que define como ativar o comportamento.

        :param percepcao: A perceção que desencadeia a ativação do comportamento.
        :return: Ação associada à ativação do comportamento.
        """
        pass
