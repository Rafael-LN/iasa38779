from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao:
    """
    Classe que representa a solução de um problema de procura.
    Contém o percurso desde o estado inicial até o estado final, bem como o custo total da solução.
    """

    def __init__(self, no_final):
        """
        Inicializa uma nova instância de Solucao.

        Parâmetros:
        no_final: O nó final da solução encontrada.

        Funcionalidade:
        Este construtor inicializa a solução construindo o percurso do estado inicial até o estado final.
        O percurso é construído a partir dos nós antecessores do nó final.
        """
        self.__no_final = no_final
        self.__percurso = []
        no = no_final

        # Construir o percurso da solução
        while no.antecessor:
            # Criar um passo da solução a partir do estado do nó antecessor e do operador aplicado
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            # Inserir o passo na primeira posição da lista de percurso
            self.__percurso.insert(0, passo)
            # Atualizar o nó atual para o nó antecessor
            no = no.antecessor

    @property
    def dimensao(self):
        """
        Obtém a dimensão da solução, ou seja, o número de passos no percurso.

        Retorna:
        O número de passos na solução.

        Funcionalidade:
        Este método retorna a dimensão da solução, que é o tamanho da lista de percurso.
        """
        return len(self.__percurso)

    @property
    def custo(self):
        """
        Obtém o custo total da solução.

        Retorna:
        O custo total da solução.

        Funcionalidade:
        Este método retorna o custo acumulado do nó final, que representa o custo total da solução.
        """
        return self.__no_final.custo

    def __iter__(self):
        """
        Retorna um iterador para percorrer os passos da solução.

        Retorna:
        Um iterador para a lista de percurso.

        Funcionalidade:
        Este método permite iterar sobre os passos da solução usando um loop.
        """
        return iter(self.__percurso)

    def __getitem__(self, index):
        """
        Obtém um passo da solução pelo índice.

        Parâmetros:
        index: O índice do passo a ser obtido.

        Retorna:
        O passo da solução correspondente ao índice fornecido.

        Funcionalidade:
        Este método permite acessar um passo específico da solução pelo índice, suportando a indexação da lista de percurso.
        """
        return self.__percurso[index]
