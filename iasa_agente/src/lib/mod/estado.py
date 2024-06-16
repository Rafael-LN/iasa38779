from abc import ABC, abstractmethod

class Estado(ABC):
    """
    Classe abstrata que define a interface para representar um estado no espaço de estados.
    Esta classe deve ser herdada por classes que implementam estados específicos, fornecendo uma representação única de cada estado.
    """

    @abstractmethod
    def id_valor(self):
        """
        Retorna um valor que identifica unicamente o estado.

        Retorna:
        Um valor único que representa o estado.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer uma representação única do estado,
        que pode ser utilizada para comparações e hashing.
        """
        pass

    def __eq__(self, outro):
        """
        Verifica a igualdade entre este estado e outro estado.

        Parâmetros:
        outro: O outro estado a ser comparado.

        Retorna:
        True se os estados forem iguais, False caso contrário.

        Funcionalidade:
        Este método verifica se o outro objeto é uma instância de Estado e compara os valores únicos dos estados
        utilizando o método id_valor.
        """
        return isinstance(outro, Estado) and self.id_valor() == outro.id_valor()

    def __hash__(self):
        """
        Retorna o valor de hash do estado.

        Retorna:
        O valor de hash do estado.

        Funcionalidade:
        Este método retorna o valor de hash do valor único do estado obtido pelo método id_valor.
        Isso permite que estados sejam utilizados em coleções baseadas em hash, como conjuntos e dicionários.
        """
        return hash(self.id_valor())
