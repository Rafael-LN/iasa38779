from plan.plano import Plano

class PlanoPEE(Plano):
    """
    Classe que representa um plano gerado pelo planeador PEE (Procura em Espaços de Estados).
    Herda da classe Plano e armazena a sequência de passos (ações) necessários para alcançar o objetivo.
    """

    def __init__(self, solucao):
        """
        Inicializa uma nova instância do PlanoPEE com base na solução fornecida.

        Parâmetros:
        solucao: Lista de passos que constituem a solução encontrada pelo mecanismo de procura.

        Funcionalidade:
        Este construtor inicializa o atributo __passos, que armazena a sequência de passos do plano.
        Cada passo é extraído da solução fornecida.
        """
        self.__passos = [passo for passo in solucao]

    def obter_accao(self, estado):
        """
        Obtém a ação correspondente a um estado específico.

        Parâmetros:
        estado: O estado para o qual se pretende obter a ação correspondente.

        Retorna:
        O operador (ação) correspondente ao estado fornecido, ou None se o estado não for encontrado na lista de passos.

        Funcionalidade:
        Este método percorre a lista de passos e verifica se o estado do passo coincide com o estado fornecido.
        Se encontrar uma correspondência, retorna o operador associado a esse passo.
        Caso contrário, retorna None.
        """
        for passo in self.__passos:
            if passo.estado == estado:
                return passo.operador
        return None

    def validar_estado(self, estado):
        """
        Verifica se um determinado estado está presente na lista de passos do plano.

        Parâmetros:
        estado: O estado a ser validado.

        Retorna:
        True se o estado estiver presente na lista de passos, False caso contrário.

        Funcionalidade:
        Este método percorre a lista de passos e verifica se o estado do passo coincide com o estado fornecido.
        Se encontrar uma correspondência, retorna True, indicando que o estado é válido dentro do plano.
        Caso contrário, retorna False.
        """
        for passo in self.__passos:
            if passo.estado == estado:
                return True
        return False

    def mostrar(self, vista):
        """
        Exibe a sequência de passos do plano utilizando uma vista fornecida.

        Parâmetros:
        vista: Objeto responsável por exibir a visualização dos passos.

        Funcionalidade:
        Este método percorre a lista de passos e, para cada passo, utiliza a vista fornecida para mostrar a posição do estado e o ângulo do operador.
        Se a lista de passos não estiver vazia, cada passo é exibido através da função mostrar_vector da vista.
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
