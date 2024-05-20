class MecUtil:
    """
    Classe MecUtil responsável por calcular a utilidade em um Processo de Decisão Markoviano (PDM).

    Atributos:
        __modelo (ModeloPDM): Modelo PDM contendo estados, ações, transições e recompensas.
        __gama (float): Taxa de desconto para recompensas diferidas no tempo.
        __delta_max (float): Limiar de convergência para a diferença máxima de atualização das utilidades.
    """
    
    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa a classe MecUtil com o modelo PDM, a taxa de desconto e o limiar de convergência.

        Args:
            modelo (ModeloPDM): Modelo PDM contendo estados, ações, transições e recompensas.
            gama (float): Taxa de desconto para recompensas diferidas no tempo.
            delta_max (float): Limiar de convergência para a diferença máxima de atualização das utilidades.
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
    def utilidade(self):
        """
        Calcula a utilidade de cada estado usando iteração de valor.

        Este método implementa a técnica de Iteração de Valor para calcular a utilidade dos estados num
        Processo de Decisão Markoviano (PDM). Inicialmente, as utilidades de todos os estados são definidas
        como zero. O método então itera sobre cada estado, calculando a utilidade esperada como o valor máximo
        das utilidades das ações possíveis, utilizando a função `util_accao`. A iteração continua até que a 
        diferença máxima entre as utilidades atualizadas e as utilidades anteriores seja menor que um limiar
        de convergência (`delta_max`).

        Returns:
            Valor da utilidade de estado para a política óptima
        """
        S = self.__modelo.S
        A = self.__modelo.A
        U = {s: 0 for s in S()}

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
        Método auxiliar para calcular a utilidade de um estado seguindo a
        política ótima, obtendo a utilidade de uma ação através de um somatório.

        Este método calcula a soma do produto da probabilidade de transição de
        estado pela recompensa esperada na transição de s para sn por meio de a,
        adicionada ao produto do fator gama pela utilidade do estado sucessor.
        A fórmula utilizada é: sum(T(s, a, s') * (R(s, a, s') + gama * U(s'))).
        
        Args:
            s (Estado): estado atual no modelo do mundo.
            a (Operador): ação que possibilita a transição para o próximo estado.
            U (dict): dicionário contendo a utilidade dos estados anteriores.
            
        Returns:
            valor do somatório calculado
        """
        T = self.__modelo.T
        R = self.__modelo.R
        gama = self.__gama

        return sum(T(s, a, sn) * (R(s, a, sn) + gama * U[sn]) for sn in self.__modelo.S())