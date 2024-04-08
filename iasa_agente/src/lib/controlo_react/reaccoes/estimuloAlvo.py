from ecr.estimulo import Estimulo


class EstimuloAlvo(Estimulo):
    
    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama
        
    def detectar(self, percepcao):
        return percepcao[self.__direccao].distancia ** self.__gama
        
        