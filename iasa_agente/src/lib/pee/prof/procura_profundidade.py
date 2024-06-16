from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """
    Classe que implementa o algoritmo de procura em profundidade.
    Herda da classe MecanismoProcura e utiliza uma fronteira LIFO (Last In, First Out) para a exploração dos nós.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ProcuraProfundidade.

        Funcionalidade:
        Este construtor chama o construtor da classe base MecanismoProcura com uma fronteira LIFO e inicializa o atributo __nos_mem_max
        para rastrear o número máximo de nós na memória durante a procura.
        """
        super().__init__(FronteiraLIFO())
        self.__nos_mem_max = 0

    def _memorizar(self, no):
        """
        Insere um nó na fronteira de exploração.

        Parâmetros:
        no: O nó a ser inserido na fronteira.

        Funcionalidade:
        Este método insere o nó na fronteira de exploração e atualiza o número máximo de nós na memória se a dimensão atual exceder o valor máximo anterior.
        """
        self._fronteira.inserir(no)
        
        if self.dimensao > self.__nos_mem_max:
            self.__nos_mem_max = self.dimensao

    def nos_memoria(self):
        """
        Obtém o número máximo de nós que foram mantidos na memória durante a procura.

        Retorna:
        O número máximo de nós na memória.

        Funcionalidade:
        Este método retorna o valor do número máximo de nós que foram armazenados na memória ao longo da execução do algoritmo de procura em profundidade.
        """
        return self.__nos_mem_max
