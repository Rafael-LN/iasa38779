from pdm.mec_util import MecUtil

class PDM:
    """
    Classe que representa um Processo de Decisão Markoviano (PDM).
    Utiliza um mecanismo de utilidade (MecUtil) para calcular a utilidade dos estados e derivar a política ótima.
    """

    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa uma nova instância de PDM.

        Parâmetros:
        modelo: O modelo PDM que define os estados, ações, transições e recompensas.
        gama: O fator de desconto utilizado no cálculo da utilidade.
        delta_max: O valor máximo de variação (delta) para o critério de convergência.

        Funcionalidade:
        Este construtor inicializa o modelo PDM, o mecanismo de utilidade, o fator de desconto e o valor máximo de variação para o critério de convergência.
        """
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):
        """
        Calcula a política ótima com base na utilidade dos estados.

        Parâmetros:
        U: Um dicionário contendo a utilidade de cada estado.

        Retorna:
        Um dicionário que mapeia cada estado à ação ótima correspondente.

        Funcionalidade:
        Este método determina a ação que maximiza a utilidade esperada para cada estado,
        utilizando a utilidade calculada previamente. A política ótima é derivada da maximização da utilidade esperada.
        """
        A = self.__modelo.A
        S = self.__modelo.S
        politica = {}

        for s in S():
            # Determina a ação que maximiza a utilidade esperada
            melhor_acao = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))
            politica[s] = melhor_acao

        return politica
    
    def resolver(self):
        """
        Resolve o PDM, calculando a utilidade dos estados e a política ótima.

        Retorna:
        Uma tupla contendo o dicionário de utilidades dos estados e a política ótima.

        Funcionalidade:
        Este método calcula a utilidade dos estados utilizando o mecanismo de utilidade (MecUtil) e, em seguida,
        determina a política ótima com base nas utilidades calculadas. Retorna ambos os resultados.
        """
        U = self.__mec_util.utilidade()
        return U, self.politica(U)
