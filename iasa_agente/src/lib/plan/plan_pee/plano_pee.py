from plan.plano import Plano

class PlanoPEE(Plano):
    """
    Classe que representa um plano de execução para um Problema de Estado Espaço.

    Esta classe estende a classe abstrata Plano e é projetada para representar um plano específico para resolver
    um Problema de Estado Espaço.

    Atributos:
        __passos: Uma lista de passos que compõem o plano de execução.

    Métodos:
        __init__: Inicializa o plano de execução com a solução fornecida.
        obter_accao: Obtém a próxima ação do plano de execução com base no estado atual.
        mostrar: Mostra visualmente os passos do plano de execução em uma vista.
    """

    def __init__(self, solucao):
        """
        Inicializa o plano de execução com a solução fornecida.

        Args:
            solucao: A solução gerada para o problema, consistindo em uma sequência de passos.
        """
        self.__passos = [passo for passo in solucao]
        
    def obter_accao(self, estado):
        """
        Obtém a próxima ação do plano de execução com base no estado atual.

        Args:
            estado: O estado atual do sistema.

        Returns:
            A próxima ação a ser executada, se houver, ou None caso o plano tenha sido concluído.
        """
        if self.__passos:
            passo = self.__passos.pop()
            if passo.estado == estado:
                return passo.operador
    
    def mostrar(self, vista):
        """
        Mostra visualmente os passos do plano de execução de uma vista.

        Args:
            vista: A vista na qual mostrar os passos do plano.
        """
        if self.__passos:
            # Mostrar passos do plano como vetores
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
