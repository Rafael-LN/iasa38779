from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao():
    """
    A classe Solucao é responsável por encapsular o percurso da 
    solução encontrada a partir de um nó final, permitindo 
    a iteração e o acesso indexado aos passos da solução, 
    bem como fornecer a dimensão e o custo total do percurso.
    """
    def __init__(self, no_final):
        """
        Inicializa a solução a partir do nó final fornecido.
        
        Este método constrói o percurso desde o nó inicial até ao nó final, 
        armazenando cada passo da solução numa lista de passos. Cada passo 
        representa uma transição de estado gerada por um operador.

        Parâmetros:
        no_final (No): O nó final da solução encontrada.
        """
        self.__no_final = no_final
        self.__percurso = []
        no = no_final
        
        # Construir o percurso da solução
        while no.antecessor():
            # Criar um passo da solução a partir do estado do nó antecessor e do operador aplicado
            passo = PassoSolucao(no.antecessor().estado, no.operador)
            # Inserir o passo na primeira posição da lista de percurso
            self.__percurso.insert(0, passo)
            # Atualizar o nó atual para o nó antecessor
            no = no.antecessor()
        
    @property
    def dimensao(self):
        """
        Retorna a dimensão da solução.
        
        A dimensão da solução é o número de passos (transições de estado) 
        necessários para chegar ao nó final a partir do nó inicial.

        Retorna:
        int: O número de passos na solução.
        """
        return len(self.__percurso)
    
    @property
    def custo(self):
        """
        Retorna o custo total da solução.
        
        O custo total é acumulado desde o estado inicial até ao estado 
        do nó final.

        Retorna:
        float: O custo total da solução.
        """
        return self.__no_final.custo

    def __iter__(self):
        """
        Permite a iteração sobre os passos da solução.
        
        Retorna:
        iterator: Um iterador sobre a lista de passos da solução.
        """
        return iter(self.__percurso)

    def __getitem__(self, index):
        """
        Permite o acesso indexado aos passos da solução.
        
        Parâmetros:
        index (int): O índice do passo a ser retornado.

        Retorna:
        PassoSolucao: O passo da solução na posição especificada.
        """
        return self.__percurso[index]
