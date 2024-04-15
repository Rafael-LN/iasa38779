class Solucao():
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__percurso = []
        no = no_final
        
        #TODO
        '''
        Enquanto houver nó antecessor
            criar passo
            inserir passo no percurso na primeira posição da estrutura
            atualizar o nó
        '''
        
    @property
    def dimensao(self):
        return len(self.__percurso)
    
    @property
    def custo(self):
        return self.__no_final.custo

    def __iter__(self):
        return iter(self.__percurso)

    def __getitem__(self, index):
        return self.__percurso[index]