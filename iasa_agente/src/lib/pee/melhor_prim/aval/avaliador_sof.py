from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """
    Classe que implementa um avaliador para o algoritmo de procura Sôfrega (Greedy Search).
    Herda da classe AvaliadorHeur e utiliza uma heurística para calcular a prioridade dos nós.
    """

    def prioridade(self, no):
        """
        Calcula a prioridade de um nó com base na heurística.

        Parâmetros:
        no: O nó cuja prioridade será calculada.

        Retorna:
        O valor heurístico do estado do nó.

        Funcionalidade:
        Este método retorna o valor heurístico do estado do nó, calculado pela função heurística.
        A prioridade é determinada exclusivamente pela estimativa heurística do custo para atingir o objetivo,
        típica do algoritmo de procura Sôfrega, que sempre expande o nó com a menor estimativa heurística.
        """
        return self._heuristica.h(no.estado)
