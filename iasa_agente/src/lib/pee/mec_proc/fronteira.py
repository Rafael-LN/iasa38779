from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Classe abstrata que define uma fronteira para armazenar nós de busca.

    Atributos:
        _nos (list): Uma lista para armazenar nós de busca.

    Métodos:
        vazia: Propriedade que verifica se a fronteira está vazia.
        dimensao: Propriedade que retorna a dimensão (tamanho) da fronteira.
        iniciar: Método para inicializar a fronteira.
        inserir: Método abstrato para inserir um nó na fronteira.
        remover: Método para remover um nó da fronteira.
    """

    def __init__(self):
        """
        Inicializa a fronteira com uma lista vazia de nós.
        """
        self._nos = []

    @property
    def vazia(self):
        """
        Verifica se a fronteira está vazia.

        Retorno:
            True se a fronteira estiver vazia, False caso contrário.
        """
        return len(self._nos) == 0

    @property
    def dimensao(self):
        """
        Retorna a dimensão (tamanho) da fronteira.

        Retorno:
            O tamanho da fronteira.
        """
        return len(self._nos)

    def iniciar(self):
        """
        Inicializa a fronteira. Método a ser implementado pelas subclasses, se necessário.
        """
        pass

    @abstractmethod
    def inserir(self, no):
        """
        Insere um nó na fronteira. Método abstrato a ser implementado pelas subclasses.

        Args:
            no: O nó a ser inserido na fronteira.
        """
        pass

    def remover(self):
        """
        Remove um nó da fronteira.

        Retorno:
            O nó removido da fronteira.
        """
         # Verifique se a fronteira não está vazia antes de tentar remover um nó.
        if not self.vazia:
            # Remova e retorne o primeiro nó da fronteira.
            return self._nos.pop(0)
        else:
            # Se a fronteira estiver vazia, retorne None ou levante uma exceção, dependendo do comportamento desejado.
            return None
