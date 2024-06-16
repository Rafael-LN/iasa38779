from abc import ABC, abstractmethod

class Problema(ABC):
    """
    Classe abstrata que define a estrutura de um problema a ser resolvido por algoritmos de procura.
    Um problema é definido por um estado inicial, um conjunto de operadores e uma condição de objetivo.
    """

    def __init__(self, estado_inicial, operadores):
        """
        Inicializa uma nova instância de Problema.

        Parâmetros:
        estado_inicial: O estado inicial a partir do qual a procura será iniciada.
        operadores: Uma lista de operadores que podem ser aplicados para transformar estados.

        Funcionalidade:
        Este construtor inicializa o estado inicial e os operadores do problema, preparando o problema para a exploração.
        """
        self.estado_inicial = estado_inicial
        self.operadores = operadores
        
    @abstractmethod
    def objectivo(self, estado):
        """
        Verifica se um estado atende à condição de objetivo.

        Parâmetros:
        estado: O estado a ser verificado.

        Retorna:
        True se o estado atender à condição de objetivo, False caso contrário.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para definir a lógica de verificação da condição de objetivo.
        A condição de objetivo determina se a solução do problema foi alcançada.
        """
        pass
