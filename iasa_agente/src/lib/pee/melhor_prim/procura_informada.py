from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    """
    Classe que define o comportamento de uma procura informada, baseada na estratégia de Melhor-Primeiro.

    Herda de ProcuraMelhorPrim.

    Métodos:
        procurar: Método para iniciar a procura informada, definindo uma heurística e chamando o método de procura da classe pai.
    """

    def procurar(self, problema, heuristica):
        """
        Inicia a procura informada, configurando a heurística e chamando o método de procura da classe pai.

        Args:
            problema: O problema a ser resolvido.
            heuristica: A heurística a ser usada na procura.
        
        Returns:
            O nó solução encontrado pela procura.
        """
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
