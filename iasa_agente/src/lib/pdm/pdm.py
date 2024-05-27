from pdm.mec_util import MecUtil

class PDM:
    """
    A classe PDM representa um modelo de Processos de Decisão de Markov (PDM) para o planeamento e determinação de políticas ótimas.

    Atributos:
        __modelo: Instância do modelo que define os estados e ações do PDM.
        __mec_util: Instância de MecUtil que auxilia no cálculo das utilidades e das políticas.

    Métodos:
        __init__(self, modelo, gama, delta_max): Inicializa a instância da classe com os parâmetros fornecidos.
        politica(self, U): Determina a política ótima para um dado vetor de utilidades.
        resolver(self): Calcula as utilidades dos estados e determina a política ótima.
    """

    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa uma instância da classe PDM.

        Parâmetros:
            modelo: Instância do modelo que define os estados e ações do PDM.
            gama (float): Fator de desconto para recompensas diferidas.
            delta_max (float): Critério de convergência para a diferença máxima na atualização das utilidades.

        Este método também inicializa uma instância de MecUtil para auxiliar nos cálculos das utilidades.
        """
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):
        """
        Determina a política ótima para um dado vetor de utilidades.

        Parâmetros:
            U (dict): Dicionário que mapeia estados às suas respectivas utilidades.

        Retorna:
            dict: Dicionário que mapeia estados às ações que maximizam a utilidade esperada.
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
        Calcula as utilidades dos estados e determina a política ótima.

        Este método utiliza a instância de MecUtil para calcular as utilidades e, em seguida, determina a política ótima com base nessas utilidades.

        Retorna:
            tuple: Um par contendo o dicionário de utilidades dos estados e o dicionário da política ótima.
        """
        U = self.__mec_util.utilidade()
        return U, self.politica(U)
