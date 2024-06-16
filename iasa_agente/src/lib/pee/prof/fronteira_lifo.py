from pee.mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """
    Classe que implementa uma fronteira LIFO (Last In, First Out) para algoritmos de procura.
    Herda da classe Fronteira e utiliza uma lista para armazenar os nós, onde o último nó inserido é o primeiro a ser removido.
    """

    def inserir(self, no):
        """
        Insere um nó na fronteira de exploração utilizando a estratégia LIFO.

        Parâmetros:
        no: O nó a ser inserido na fronteira.

        Funcionalidade:
        Este método insere o nó no início da lista de nós, garantindo que o nó mais recentemente adicionado será o primeiro a ser removido durante a exploração.
        A estratégia LIFO é típica de algoritmos de procura em profundidade.
        """
        self._nos.insert(0, no)
