from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Classe abstrata que define a interface para uma fronteira utilizada em algoritmos de procura.
    A fronteira armazena os nós que serão explorados durante a procura.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de Fronteira.

        Funcionalidade:
        Este construtor inicializa a fronteira chamando o método iniciar para preparar a estrutura de dados que armazenará os nós.
        """
        self.iniciar()

    @property
    def vazia(self):
        """
        Verifica se a fronteira está vazia.

        Retorna:
        True se a fronteira estiver vazia, False caso contrário.

        Funcionalidade:
        Este método verifica se a lista de nós está vazia.
        """
        return len(self._nos) == 0

    @property
    def dimensao(self):
        """
        Obtém a dimensão da fronteira, ou seja, o número de nós armazenados.

        Retorna:
        O número de nós na fronteira.

        Funcionalidade:
        Este método retorna o tamanho da lista de nós.
        """
        return len(self._nos)

    def iniciar(self):
        """
        Inicializa a fronteira de exploração.

        Funcionalidade:
        Este método cria uma nova lista vazia para armazenar os nós que serão explorados.
        """
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """
        Insere um nó na fronteira de exploração.

        Parâmetros:
        no: O nó a ser inserido.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para definir a lógica de inserção de nós na fronteira.
        """
        pass

    def remover(self):
        """
        Remove e retorna o primeiro nó da fronteira de exploração.

        Retorna:
        O primeiro nó da fronteira, ou None se a fronteira estiver vazia.

        Funcionalidade:
        Este método remove e retorna o primeiro nó da lista de nós, se a fronteira não estiver vazia.
        Se a fronteira estiver vazia, retorna None.
        """
        if not self.vazia:
            return self._nos.pop(0)
        else:
            return None
