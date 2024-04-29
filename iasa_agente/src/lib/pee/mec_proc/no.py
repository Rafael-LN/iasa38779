class No:
    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """
        Inicializa um nó com o estado do problema, operador utilizado, nó antecessor e custo associado.

        Args:
            estado: O estado do problema associado ao nó.
            operador: O operador utilizado para chegar a este estado (opcional).
            antecessor: O nó antecessor que leva a este nó (opcional).
            custo: O custo associado a este nó (padrão é 0).
        """
        self.estado = estado
        self.operador = operador
        self.antecessor = antecessor
        self._custo = custo
        self._profundidade = 0
    
    @property
    def custo(self):
        """
        Retorna o custo associado a este nó.

        Retorno:
            O custo associado a este nó.
        """
        return self._custo

    @property
    def profundidade(self):
        """
        Retorna a profundidade deste nó na árvore de busca.

        Retorno:
            A profundidade deste nó na árvore de busca.
        """
        return self._profundidade
    
    @property
    def antecessor(self):
        """
        Retorna o nó antecessor que leva a este nó.

        Retorno:
            O nó antecessor que leva a este nó.
        """
        return self._antecessor
    
    def __eq__(self, outro):
        """
        Verifica se dois nós são iguais.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se os nós forem iguais, False caso contrário.
        """
        return self.estado == outro.estado and self.operador == outro.operador \
               and self.antecessor == outro.antecessor and self.custo == outro.custo \
               and self.profundidade == outro.profundidade

    def __ne__(self, outro):
        """
        Verifica se dois nós são diferentes.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se os nós forem diferentes, False caso contrário.
        """
        return not self.__eq__(outro)

    def __lt__(self, outro):
        """
        Verifica se este nó é menor que outro nó.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se este nó for menor que o outro, False caso contrário.
        """
        return (self.custo, self.profundidade) < (outro.custo, outro.profundidade)

    def __le__(self, outro):
        """
        Verifica se este nó é menor ou igual ao outro nó.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se este nó for menor ou igual ao outro, False caso contrário.
        """
        return (self.custo, self.profundidade) <= (outro.custo, outro.profundidade)

    def __gt__(self, outro):
        """
        Verifica se este nó é maior que o outro nó.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se este nó for maior que o outro, False caso contrário.
        """
        return (self.custo, self.profundidade) > (outro.custo, outro.profundidade)

    def __ge__(self, outro):
        """
        Verifica se este nó é maior ou igual ao outro nó.

        Args:
            outro: O outro nó a ser comparado.

        Retorno:
            True se este nó for maior ou igual ao outro, False caso contrário.
        """
        return (self.custo, self.profundidade) >= (outro.custo, outro.profundidade)
