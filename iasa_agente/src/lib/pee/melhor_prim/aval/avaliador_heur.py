from pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorHeur(Avaliador):
    """
    Classe que implementa um avaliador heurístico.
    Herda da classe Avaliador e utiliza uma função heurística para calcular a prioridade dos nós.
    """

    def definir_heuristica(self, heuristica):
        """
        Define a função heurística a ser utilizada pelo avaliador.

        Parâmetros:
        heuristica: A função heurística que será utilizada para calcular a prioridade dos nós.

        Funcionalidade:
        Este método armazena a função heurística fornecida, que será utilizada posteriormente para avaliar a prioridade dos nós
        durante a procura. A função heurística estima o custo restante para atingir o objetivo a partir de um determinado estado.
        """
        self._heuristica = heuristica
