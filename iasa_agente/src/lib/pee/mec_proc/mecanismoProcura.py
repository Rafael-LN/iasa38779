from abc import ABC, abstractmethod

from pee.mec_proc.no import No

class MecanismoProcura(ABC):
    """
    Classe abstrata que define um mecanismo de procura para resolver problemas.

    Atributos:
        _fronteira: A fronteira para armazenar nós de busca.
        __nos_processados: O número de nós processados durante a procura.

    Métodos:
        nos_processados: Propriedade para obter o número de nós processados.
        nos_memoria: Propriedade abstrata para obter o número máximo de nós em memória.
        _iniciar_memoria: Método para inicializar a memória de busca.
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

        Returns:
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
        Inicializa a memória de busca. Método a ser implementado pelas subclasses, se necessário.
        """
        pass

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
        Realiza a procura do problema. Método abstrato a ser implementado pelas subclasses.

        Args:
            problema: O problema a ser resolvido.
        """
        pass

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
        # Implementação genérica para expandir um nó
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_successor = No(estado_suc, operador, no, custo)
                sucessores.append(no_successor)
        return sucessores
