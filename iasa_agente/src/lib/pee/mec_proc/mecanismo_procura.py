from abc import ABC, abstractmethod
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

    def iniciar_memoria(self):
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
        # Inicializa as estruturas de memória de procura
        self.iniciar_memoria()

        # Insere o nó inicial na fronteira de exploração
        no_inicial = No(problema.estado_inicial)
        self._fronteira.inserir(no_inicial)

        # Enquanto a fronteira não estiver vazia
        while not self._fronteira.vazia:
            # Remove o próximo nó da fronteira para expansão
            no_atual = self._fronteira.remover()

            # Verifica se o nó é um objetivo
            if problema.objectivo(no_atual.estado):
                # Se sim, retorna o nó de solução
                return Solucao(no_atual)

            # Expande o nó atual e adiciona os nós sucessores na fronteira
            sucessores = self._expandir(problema, no_atual)
            for suc in sucessores:
                self._fronteira.inserir(suc)

            # Memoriza o nó atual
            self._memorizar(no_atual)

            # Incrementa o contador de nós processados
            self.__nos_processados += 1

        # Se a fronteira ficar vazia e nenhum objetivo for encontrado, retorna None
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
        sucessores = []  # Lista para armazenar os nós sucessores
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(no.estado, estado_suc)
                no_successor = No(no.estado, operador, no, custo)
                sucessores.append(no_successor)
        return sucessores
