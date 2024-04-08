from ecr.estimulo import Estimulo


class EstimuloAlvo(Estimulo):
    
    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama
        
    def detectar(self, percepcao):
        perDir = percepcao[self.__direccao]
        if(perDir.elemento == "A"):
            return perDir.distancia ** self.__gama
        return 0
        