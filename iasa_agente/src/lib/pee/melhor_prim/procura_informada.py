from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    """
    Classe que implementa um algoritmo de procura informada.
    Herda da classe ProcuraMelhorPrim e permite a utilização de uma heurística específica para guiar a procura.
    """

    def procurar(self, problema, heuristica):
        """
        Realiza a procura de uma solução utilizando uma heurística especificada.

        Parâmetros:
        problema: O problema de planeamento a ser resolvido.
        heuristica: A função heurística a ser utilizada para avaliar a prioridade dos nós.

        Retorna:
        Uma instância de Solucao se uma solução for encontrada, ou None se não houver solução.

        Funcionalidade:
        Este método define a heurística a ser utilizada pelo avaliador, e então chama o método procurar da classe base
        para realizar a procura com a heurística especificada.
        """
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
