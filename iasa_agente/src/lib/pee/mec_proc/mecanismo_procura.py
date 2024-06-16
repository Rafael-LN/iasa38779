from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

class MecanismoProcura(ABC):
    """
    Classe abstrata que define a estrutura base para mecanismos de procura em espaços de estados.
    Esta classe fornece os métodos básicos para inicializar a memória, memorizar nós e realizar a procura.
    """

    def __init__(self, fronteira):
        """
        Inicializa uma nova instância de MecanismoProcura.

        Parâmetros:
        fronteira: A fronteira de exploração utilizada pelo mecanismo de procura.

        Funcionalidade:
        Este construtor inicializa a fronteira de exploração e o contador de nós processados.
        """
        self._fronteira = fronteira
        self.__nos_processados = 0

    @property
    def nos_processados(self):
        """
        Obtém o número de nós processados durante a procura.

        Retorna:
        O número de nós processados.

        Funcionalidade:
        Este método retorna o valor do contador de nós processados.
        """
        return self.__nos_processados

    @property
    @abstractmethod
    def nos_memoria(self):
        """
        Método abstrato para obter o número de nós na memória.

        Retorna:
        O número de nós atualmente armazenados na memória.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer o número de nós mantidos na memória.
        """
        pass

    def _iniciar_memoria(self):
        """
        Inicializa a memória e a fronteira de exploração.

        Funcionalidade:
        Este método reinicia o contador de nós processados e inicializa a fronteira de exploração de acordo com o tipo de procura.
        """
        self.__nos_processados = 0
        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        """
        Memoriza um nó na fronteira de exploração.

        Parâmetros:
        no: O nó a ser memorizado.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para definir a lógica de memorização de nós na fronteira de exploração.
        """
        pass

    def procurar(self, problema):
        """
        Realiza a procura de uma solução para o problema.

        Parâmetros:
        problema: O problema de planeamento a ser resolvido.

        Retorna:
        Uma instância de Solucao se uma solução for encontrada, ou None se não houver solução.

        Funcionalidade:
        Este método inicializa a memória, cria o nó inicial e realiza a procura utilizando a fronteira de exploração.
        Expande os nós até encontrar uma solução ou esgotar a fronteira.
        """
        self._iniciar_memoria()
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
        Expande um nó, gerando seus sucessores.

        Parâmetros:
        problema: O problema de planeamento que define os operadores.
        no: O nó a ser expandido.

        Retorna:
        Um gerador de nós sucessores.

        Funcionalidade:
        Este método aplica todos os operadores ao estado do nó atual, gerando estados sucessores.
        Calcula o custo de transição e cria novos nós sucessores.
        """
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            if estado_sucessor is not None:
                custo = no.custo + operador.custo(no.estado, estado_sucessor)
                yield No(estado_sucessor, operador, no, custo)
