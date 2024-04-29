from mod.estado import Estado


class EstadoContagem(Estado):
    def __init__(self, valor):
        self.__valor = valor
        
    def id_valor(self):
        return self.__valor
    
    @property
    def valor(self):
        return self.__valor    