class No:
    """
    Classe que representa um nó em um espaço de estados utilizado em algoritmos de procura.
    Um nó contém um estado, um operador que levou a esse estado, um antecessor, o custo acumulado e a profundidade do nó na árvore de procura.
    """

    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """
        Inicializa uma nova instância de No.

        Parâmetros:
        estado: O estado representado por este nó.
        operador: O operador que foi aplicado para alcançar este estado (padrão é None).
        antecessor: O nó antecessor na árvore de procura (padrão é None).
        custo: O custo acumulado para alcançar este estado (padrão é 0).

        Funcionalidade:
        Este construtor inicializa os atributos do nó, calculando a profundidade com base no antecessor.
        """
        self.estado = estado
        self.operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__profundidade = antecessor.profundidade + 1 if antecessor else 0

    @property
    def custo(self):
        """
        Obtém o custo acumulado para alcançar este nó.

        Retorna:
        O custo acumulado do nó.

        Funcionalidade:
        Este método retorna o valor do custo acumulado armazenado no nó.
        """
        return self.__custo

    @property
    def profundidade(self):
        """
        Obtém a profundidade do nó na árvore de procura.

        Retorna:
        A profundidade do nó.

        Funcionalidade:
        Este método retorna o valor da profundidade do nó, calculada com base no antecessor.
        """
        return self.__profundidade

    @property
    def antecessor(self):
        """
        Obtém o nó antecessor na árvore de procura.

        Retorna:
        O nó antecessor.

        Funcionalidade:
        Este método retorna o nó antecessor que levou a este nó.
        """
        return self.__antecessor

    def __eq__(self, outro):
        """
        Verifica a igualdade entre este nó e outro nó.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se os nós forem iguais, False caso contrário.

        Funcionalidade:
        Este método compara o estado, operador, antecessor, custo e profundidade dos dois nós para determinar a igualdade.
        """
        return self.estado == outro.estado and self.operador == outro.operador \
               and self.antecessor == outro.antecessor and self.custo == outro.custo \
               and self.profundidade == outro.profundidade

    def __ne__(self, outro):
        """
        Verifica a desigualdade entre este nó e outro nó.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se os nós forem diferentes, False caso contrário.

        Funcionalidade:
        Este método utiliza a negação do método __eq__ para determinar a desigualdade.
        """
        return not self.__eq__(outro)

    def __lt__(self, outro):
        """
        Compara este nó com outro nó para verificar se é menor.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se este nó for menor que o outro nó, False caso contrário.

        Funcionalidade:
        Este método compara os nós com base no custo e, em caso de empate, na profundidade.
        """
        return (self.custo, self.profundidade) < (outro.custo, outro.profundidade)

    def __le__(self, outro):
        """
        Compara este nó com outro nó para verificar se é menor ou igual.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se este nó for menor ou igual ao outro nó, False caso contrário.

        Funcionalidade:
        Este método compara os nós com base no custo e, em caso de empate, na profundidade.
        """
        return (self.custo, self.profundidade) <= (outro.custo, outro.profundidade)

    def __gt__(self, outro):
        """
        Compara este nó com outro nó para verificar se é maior.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se este nó for maior que o outro nó, False caso contrário.

        Funcionalidade:
        Este método compara os nós com base no custo e, em caso de empate, na profundidade.
        """
        return (self.custo, self.profundidade) > (outro.custo, outro.profundidade)

    def __ge__(self, outro):
        """
        Compara este nó com outro nó para verificar se é maior ou igual.

        Parâmetros:
        outro: O outro nó a ser comparado.

        Retorna:
        True se este nó for maior ou igual ao outro nó, False caso contrário.

        Funcionalidade:
        Este método compara os nós com base no custo e, em caso de empate, na profundidade.
        """
        return (self.custo, self.profundidade) >= (outro.custo, outro.profundidade)
