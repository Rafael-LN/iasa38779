from pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorHeur(Avaliador):
    """
    Classe que implementa um avaliador de prioridade para procura informada baseada em heurísticas.

    Métodos:
        definir_heuristica: Define a heurística a ser utilizada pelo avaliador.
    """

    def definir_heuristica(self, heuristica):
        """
        Define a heurística a ser utilizada pelo avaliador.

        Args:
            heuristica: A função de heurística a ser definida para o avaliador.
        """
        self._heuristica = heuristica
