from pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    """
    Classe que implementa o avaliador de custo uniforme.
    Herda da classe Avaliador e fornece uma função de prioridade que retorna o custo do nó, utilizado em algoritmos de procura de custo uniforme.
    """

    def prioridade(self, no):
        """
        Calcula a prioridade de um nó com base no seu custo acumulado.

        Parâmetros:
        no: O nó cuja prioridade será calculada.

        Retorna:
        O custo acumulado do nó.

        Funcionalidade:
        Este método retorna o custo acumulado do nó, que representa a soma dos custos das transições de estado desde o estado inicial até o estado atual do nó.
        A prioridade é utilizada para ordenar os nós na fronteira de exploração, priorizando os nós com menor custo acumulado.
        """
        return no.custo
