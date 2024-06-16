from pee.prof.procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """
    Classe que implementa o algoritmo de procura em profundidade iterativa.
    Herda da classe ProcuraProfLim e realiza múltiplas buscas em profundidade limitada com profundidade crescente.
    """

    def procurar(self, problema, inc_prof, limite_prof):
        """
        Realiza a procura de uma solução utilizando a estratégia de profundidade iterativa.

        Parâmetros:
        problema: O problema de planeamento a ser resolvido.
        inc_prof: O incremento de profundidade a ser utilizado em cada iteração.
        limite_prof: A profundidade máxima a ser alcançada nas iterações.

        Retorna:
        A solução encontrada se houver, ou None se não for encontrada nenhuma solução dentro do limite de profundidade.

        Funcionalidade:
        Este método realiza buscas em profundidade limitada com profundidade crescente, começando de zero até o limite especificado.
        Em cada iteração, a profundidade máxima é aumentada pelo incremento especificado e a busca é realizada.
        Se uma solução for encontrada, é retornada imediatamente; caso contrário, a busca continua até atingir o limite de profundidade.
        """
        self.prof_max = 0  # Inicializa a profundidade máxima no método da classe base
        for i in range(0, limite_prof, inc_prof):
            self.prof_max = i
            solucao = super().procurar(problema)
            if solucao:
                return solucao
        return None
