from pee.mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """
    Classe que implementa uma fronteira FIFO (First In, First Out) para algoritmos de procura.
    Herda da classe Fronteira e utiliza uma lista para armazenar os nós, onde o primeiro nó inserido é o primeiro a ser removido.
    """

    def inserir(self, no):
        """
        Insere um nó na fronteira de exploração utilizando a estratégia FIFO.

        Parâmetros:
        no: O nó a ser inserido na fronteira.

        Funcionalidade:
        Este método adiciona o nó ao final da lista de nós, garantindo que o nó mais antigo adicionado será o primeiro a ser removido durante a exploração.
        A estratégia FIFO é típica de algoritmos de procura em largura.
        """
        self._nos.append(no)
