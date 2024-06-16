from abc import ABC, abstractmethod
from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

class MecanismoProcura(ABC):
    """
    Classe abstrata que define um mecanismo de procura para resolver problemas.

    Atributos:
        _fronteira: A fronteira para armazenar nós de busca.
        __nos_processados: O número de nós processados durante a procura.

    Métodos:
        nos_processados: Propriedade para obter o número de nós processados.
        nos_memoria: Propriedade abstrata para obter o número máximo de nós em memória.
        iniciar_memoria: Método para inicializar a memória de busca.
        _memorizar: Método abstrato para memorizar um nó durante a procura.
        procurar: Método abstrato para realizar a procura do problema.
        _expandir: Método para expandir um nó durante a procura.
    """

    def __init__(self, fronteira):
        """
        Inicializa o mecanismo de procura com a fronteira e o número de nós processados.

        Args:
            fronteira: A fronteira para armazenar nós de busca.
        """
        self._fronteira = fronteira
        self.__nos_processados = 0

    @property
    def nos_processados(self):
        """
        Obtém o número de nós processados durante a procura.

        Retorno:
            O número de nós processados durante a procura.
        """
        return self.__nos_processados

    @property
    @abstractmethod
    def nos_memoria(self):
        """
        Obtém o número máximo de nós em memória.

        Retorno:
            O número máximo de nós em memória.
        """
        pass

    def _iniciar_memoria(self):
        """
        Inicia as estruturas de memória de procura de acordo com o tipo de procura,
        incluindo a fronteira de exploração.
        """
        # Reinicia o contador de nós processados
        self.__nos_processados = 0

        # Inicializa a fronteira de exploração de acordo com o tipo de procura
        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        """
        Memoriza um nó durante a procura. Método a ser implementado pelas subclasses.

        Args:
            no: O nó a ser memorizado durante a procura.
        """
        pass

    def procurar(self, problema):
        """
        Realiza a procura do problema.

        Args:
            problema: O problema a ser resolvido.

        Retorno:
            O nó de solução encontrado ou None se a solução não for encontrada.
        """
        self.iniciar_memoria()
        no_inicial = No(problema.estado_inicial)
        self._memorizar(no_inicial)
        
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            else:
                nos_suc = self._expandir(problema, no)
                for no in nos_suc:
                    self._memorizar(no)

        return None

    def _expandir(self, problema, no):
        """
        Expande um nó durante a procura.

        Args:
            problema: O problema a ser resolvido.
            no: O nó a ser expandido durante a procura.

        Retorno:
            Uma lista de nós sucessores gerados pela expansão do nó atual.
        """
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            if estado_sucessor is not None:
                custo = no.custo + operador.custo(no.estado, estado_sucessor)
                yield No(estado_sucessor, operador, no, custo)
