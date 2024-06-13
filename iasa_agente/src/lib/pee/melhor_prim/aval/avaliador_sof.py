from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """
    A classe AvaliadorSof implementa um avaliador heurístico para algoritmos de procura gulosa (Greedy Search).

    A avaliação é baseada no custo do nó atual, priorizando nós com menor custo, típico em algoritmos de procura que utilizam estratégias ávidas para otimização.

    Herda:
        AvaliadorHeur: Classe base que define a interface e funcionalidade básica para avaliadores heurísticos.

    Métodos:
        prioridade(self, no): Retorna a prioridade de um nó com base no seu custo.
    """

    def prioridade(self, no):
        """
        Calcula a prioridade de um nó com base no seu custo.

        Este método é utilizado em algoritmos de procura gulosa onde a decisão de expansão do nó é baseada no custo atual do nó, favorecendo nós com menor custo.

        Parâmetros:
            no: O nó cuja prioridade será calculada.

        Retorna:
            float: O custo do nó, utilizado como prioridade na expansão.
        """
        return no.custo
