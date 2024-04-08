from abc import ABC, abstractmethod

class Estimulo(ABC):
    """
    Interface que representa um estímulo.
    """

    @abstractmethod    
    def detectar(self, percepcao):
        """
        Método abstrato que define como detetar um estímulo.

        :param percepcao: A perceção a ser analisada para detetar o estímulo.
        :return: Deve retornar a intensidade relacionada com a deteção do estímulo.
        """
        pass