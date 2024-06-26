from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao


class RespostaEvitar(RespostaMover):
    
    def __init__(self, dir_inicial = Direccao.ESTE):
        super().__init__(dir_inicial)
    
    def activar(self, percepcao, intensidade):
        if percepcao.contacto_obst(self._accao.direccao):
           self.__alterar_direccao(percepcao)
        
        
        return super().activar(percepcao, intensidade)
    
    
    def __alterar_direccao(self, percepcao):
        """
        Alterar direção do agente
        @param percepcao: percepção actual
        @return: direcao livre (sim/nao)
        """
        direccao_livre = self.__direccao_livre(percepcao)
        
        if direccao_livre:
            self._accao.direccao = direccao_livre
        
        return direccao_livre
    
    def __direccao_livre(self, percepcao):
        for direccao in list(Direccao):
            if not percepcao.contacto_obst(direccao):
                return direccao
        