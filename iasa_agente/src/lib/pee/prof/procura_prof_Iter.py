from pee.prof.procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """
    A classe ProcuraProfIter implementa a procura em profundidade iterativa, estendendo a classe ProcuraProfLim.

    A procura em profundidade iterativa é uma técnica que combina a profundidade limitada e a profundidade iterativa, aumentando gradualmente o limite de profundidade até encontrar uma solução ou atingir o limite máximo.

    Herda:
        ProcuraProfLim: Classe base que implementa a procura em profundidade com um limite máximo de profundidade.

    Métodos:
        procurar(self, problema, inc_prof, limite_prof): Realiza a procura em profundidade iterativa para resolver o problema fornecido.
    """

    def procurar(self, problema, inc_prof, limite_prof):
        """
        Realiza a procura em profundidade iterativa para resolver o problema fornecido.

        Este método incrementa gradualmente o limite de profundidade, realizando a procura em cada nível até encontrar uma solução ou atingir o limite máximo.

        Parâmetros:
            problema: O problema a ser resolvido, definido como um espaço de estados com operadores e objetivos.
            inc_prof (int): O incremento da profundidade a cada iteração.
            limite_prof (int): O limite máximo de profundidade para a procura.

        Retorna:
            solucao: A solução encontrada para o problema, ou None se nenhuma solução for encontrada dentro do limite de profundidade.
        """
        super().prof_max = 0  # Inicializa a profundidade máxima no método da classe base
        for i in range(0, limite_prof, inc_prof):
            super().prof_max = i
            solucao = super().procurar(problema)
            if solucao:
                return solucao
        return None
