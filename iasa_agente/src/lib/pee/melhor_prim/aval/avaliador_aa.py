from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):
    """
    Classe que implementa o avaliador para o algoritmo de procura A* (A Estrela).
    Herda da classe AvaliadorHeur e utiliza a função de avaliação f(n) = g(n) + h(n) para calcular a prioridade dos nós.
    """

    def prioridade(self, no):
        """
        Calcula a prioridade de um nó com base na função de avaliação A*.

        Parâmetros:
        no: O nó cuja prioridade será calculada.

        Retorna:
        A soma do custo acumulado (g(n)) e da estimativa heurística (h(n)) para o estado do nó.

        Funcionalidade:
        Este método retorna a prioridade do nó como a soma do custo acumulado para alcançar o nó (g(n)) e a estimativa heurística
        do custo restante para atingir o objetivo (h(n)). Esta função de avaliação é utilizada pelo algoritmo A* para garantir a exploração
        ótima e completa do espaço de estados.
        """
        return self._heuristica.h(no.estado) + no.custo
