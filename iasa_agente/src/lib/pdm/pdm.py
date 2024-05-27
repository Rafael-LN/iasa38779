from pdm.mec_util import MecUtil


class PDM:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):
        """
        Determina a política ótima para cada estado, selecionando a ação que
        maximiza a utilidade esperada.

        Este método percorre todos os estados do modelo e para cada estado,
        escolhe a ação que resulta na maior utilidade esperada, utilizando as
        utilidades fornecidas.

        @param U: dicionário com a utilidade de cada estado
        @returns: dicionário que mapeia cada estado para a melhor ação
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
        Resolve o PDM calculando as utilidades dos estados e determinando a
        política ótima baseada nessas utilidades.

        @returns: tupla contendo o dicionário de utilidades e o dicionário da política ótima
        """
        U = self.__mec_util.utilidade()
        return U, self.politica(U)