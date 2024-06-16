from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    """
    Classe que implementa o algoritmo de procura em grafos.
    Herda da classe MecanismoProcura e adiciona funcionalidades específicas para a exploração de grafos,
    como o controle de nós explorados e a memória de fronteira.
    """

    def _iniciar_memoria(self):
        """
        Inicializa a memória utilizada durante a procura.

        Funcionalidade:
        Este método chama o método de inicialização de memória da classe base e inicializa um dicionário
        para rastrear os nós explorados durante a procura.
        """
        super()._iniciar_memoria()
        self._explorados = {}

    def _memorizar(self, no):
        """
        Memoriza um nó na fronteira de exploração e no conjunto de nós explorados, se aplicável.

        Parâmetros:
        no: O nó a ser memorizado.

        Funcionalidade:
        Este método insere o nó na fronteira de exploração e no conjunto de nós explorados,
        se o nó ainda não tiver sido explorado ou se deve ser mantido na fronteira.
        """
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

    def _manter(self, no):
        """
        Determina se um nó deve ser mantido na fronteira de exploração.

        Parâmetros:
        no: O nó a ser avaliado.

        Retorna:
        True se o nó deve ser mantido, False caso contrário.

        Funcionalidade:
        Este método verifica se o nó deve ser mantido na fronteira de exploração.
        Um nó é mantido se o estado do nó ainda não tiver sido explorado.
        """
        return no.estado not in self._explorados

    def nos_memoria(self):
        """
        Obtém o número de nós que foram processados e armazenados na memória durante a procura.

        Retorna:
        O número de nós processados.

        Funcionalidade:
        Este método retorna o tamanho do conjunto de nós processados, que inclui todos os nós que foram explorados
        e armazenados na memória ao longo da execução do algoritmo de procura em grafos.
        """
        return len(self._nos_processados)
