from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    def __init__(self, direccao, intensidade = 1):
        self.direccao = direccao
        self.intensidade = intensidade
        
    def detectar(self, percepcao):
        return self.intensidade if percepcao.contacto_obst(self.direccao) else 0