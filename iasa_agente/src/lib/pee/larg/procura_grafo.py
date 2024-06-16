from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    """
    Classe que implementa um mecanismo de procura em grafo.

    Métodos:
        _iniciar_memoria: Inicializa a memória para a procura.
        _memorizar: Memoriza um nó durante a procura.
        _manter: Verifica se um nó deve ser mantido na memória.
        nos_memoria: Retorna o número de nós na memória.
    """

    def _iniciar_memoria(self):
        """
        Inicializa a memória para a procura.
        """
        super()._iniciar_memoria()
        self._explorados = {}

    def _memorizar(self, no):
        """
        Memoriza um nó durante a procura.

        Args:
            no: O nó a ser memorizado.
        """
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

    def _manter(self, no):
        """
        Verifica se um nó deve ser mantido na memória.

        Args:
            no: O nó a ser verificado.

        Retorno:
            True se o nó deve ser mantido, False caso contrário.
        """
        return no.estado not in self._explorados

    def nos_memoria(self):
        """
        Retorna o número de nós na memória.

        Retorno:
            O número de nós na memória.
        """
        return len(self._nos_processados)
