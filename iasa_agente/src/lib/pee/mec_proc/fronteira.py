from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Classe abstrata que define uma fronteira para armazenar nós durante a pesquisa.

    Métodos Abstratos:
        inserir(no): Método abstrato para inserir um nó na fronteira.

    Attributes:
        _nos: Uma estrutura de dados para armazenar os nós na fronteira.

    Propriedades:
        vazia: Retorna True se a fronteira estiver vazia, False caso contrário.
        dimensao: Retorna a dimensão da estrutura de nós (fronteira).

    Métodos:
        iniciar(): Método para iniciar a fronteira.
        remover(): Método para remover e retornar um nó da fronteira.

    Nota:
        O método abstrato `inserir` deve ser implementado.
    """

    def __init__(self):
        """
        Inicializa a fronteira.
        """
        self._nos

    @property
    def vazia(self):
        """
        Verifica se a fronteira está vazia.

        Returns:
            True se a fronteira estiver vazia, False caso contrário.
        """
        return len(self._nos) == 0

    @property
    def dimensao(self):
        """
        Retorna a dimensão da estrutura de nós (fronteira).

        Returns:
            A dimensão da estrutura de nós.
        """
        return len(self._nos)
    
    def iniciar(self):
        """
        Inicia a fronteira.
        """
        pass
    
    @abstractmethod
    def inserir(self, no):
        """
        Insere um nó na fronteira.

        Args:
            no: O nó a ser inserido na fronteira.
        """
        pass
    
    def remover(self):
        """
        Remove e retorna um nó da fronteira.

        Returns:
            O nó removido da fronteira.
        """
        pass
