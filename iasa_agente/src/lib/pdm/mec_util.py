class MecUtil:
    """
    Classe que implementa o mecanismo de cálculo de utilidade para Processos de Decisão Markovianos (PDM).
    Utiliza o método de iteração de valores para calcular a utilidade dos estados.
    """

    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa uma nova instância de MecUtil.

        Parâmetros:
        modelo: O modelo PDM que define os estados, ações, transições e recompensas.
        gama: O fator de desconto utilizado no cálculo da utilidade.
        delta_max: O valor máximo de variação (delta) para o critério de convergência.

        Funcionalidade:
        Este construtor inicializa o modelo PDM, o fator de desconto e o valor máximo de variação para o critério de convergência.
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        """
        Calcula a utilidade dos estados utilizando o método de iteração de valores.

        Retorna:
        Um dicionário contendo a utilidade de cada estado.

        Funcionalidade:
        Este método calcula a utilidade de cada estado no PDM utilizando o método de iteração de valores.
        A utilidade é atualizada iterativamente até que a variação máxima (delta) entre as iterações seja menor ou igual a delta_max.
        """
        S = self.__modelo.S
        A = self.__modelo.A
        U = {s: 0.0 for s in S()}

        while True:
            Uant = U.copy()
            delta = 0

            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))

            if delta <= self.__delta_max:
                break

        return U

    def util_accao(self, s, a, U):
        """
        Calcula a utilidade de uma ação a partir de um estado dado.

        Parâmetros:
        s: O estado atual.
        a: A ação a ser avaliada.
        U: O dicionário de utilidades dos estados.

        Retorna:
        A utilidade da ação a partir do estado s.

        Funcionalidade:
        Este método calcula a utilidade de uma ação a partir de um estado dado, utilizando a função de transição,
        a função de recompensa e o fator de desconto. A utilidade da ação é a soma das utilidades ponderadas dos estados sucessores.
        """
        T = self.__modelo.T
        R = self.__modelo.R
        gama = self.__gama
        suc = self.__modelo.suc
        
        return sum(T(s, a, sn) * (R(s, a, sn) + gama * U[sn]) for sn in suc(s, a))
