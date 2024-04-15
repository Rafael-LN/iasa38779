class No():
    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        self.estado = estado
        self.operador = operador
        self.antecessor = antecessor
        self._custo = custo
        self._profundidade = 0
    
    @property
    def custo(self):
        return self._custo

    @property
    def profundidade(self):
        return self._profundidade
    
    def __eq__(self, outro):
        return self.estado == outro.estado and self.operador == outro.operador \
               and self.antecessor == outro.antecessor and self.custo == outro.custo \
               and self.profundidade == outro.profundidade

    def __ne__(self, outro):
        return not self.__eq__(outro)

    def __lt__(self, outro):
        return (self.custo, self.profundidade) < (outro.custo, outro.profundidade)

    def __le__(self, outro):
        return (self.custo, self.profundidade) <= (outro.custo, outro.profundidade)

    def __gt__(self, outro):
        return (self.custo, self.profundidade) > (outro.custo, outro.profundidade)

    def __ge__(self, outro):
        return (self.custo, self.profundidade) >= (outro.custo, outro.profundidade)