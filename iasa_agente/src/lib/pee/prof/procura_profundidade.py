from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """
    A classe ProcuraProfundidade implementa um mecanismo de procura em profundidade, estendendo a classe MecanismoProcura.

    A procura em profundidade é um método de exploração de espaço de estados onde os nós são explorados o mais profundo possível antes de retroceder. Esta classe também rastreia o número máximo de nós em memória durante a execução do algoritmo.

    Herda:
        MecanismoProcura: Classe base que define a interface e a funcionalidade básica para diferentes mecanismos de procura.

    Atributos:
        __nos_mem_max (int): Armazena o número máximo de nós em memória durante a execução da procura.

    Métodos:
        __init__(self): Inicializa a instância da classe ProcuraProfundidade.
        _memorizar(self, no): Atualiza o número máximo de nós em memória se a dimensão atual exceder o máximo registrado.
        nos_memoria(self): Retorna o número máximo de nós que foram armazenados em memória durante a execução da procura.
    """

    def __init__(self):
        """
        Inicializa uma instância da classe ProcuraProfundidade.

        Este método chama o construtor da classe base MecanismoProcura e inicializa o atributo __nos_mem_max com 0.
        """
        super().__init__(FronteiraLIFO())
        self.__nos_mem_max = 0
        
    def _memorizar(self, no):
        """
        Atualiza o número máximo de nós em memória se a dimensão atual exceder o máximo registrado.

        Este método é chamado durante a execução da procura para rastrear a quantidade de memória utilizada.

        Parâmetros:
            no: O nó atual sendo processado.
        """
        self._fronteira.inserir(no)
        
        if self.dimensao > self.__nos_mem_max:
            self.__nos_mem_max = self.dimensao
        
    def nos_memoria(self):
        """
        Retorna o número máximo de nós que foram armazenados em memória durante a execução da procura.

        Este método fornece uma métrica útil para avaliar a eficiência espacial do algoritmo de procura.

        Retorna:
            int: O número máximo de nós em memória.
        """
        return self.__nos_mem_max
