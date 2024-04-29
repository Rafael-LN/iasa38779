from random import choice
from controlo_react.reaccoes.resposta.respostaMover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao


class Explorar(Comportamento):
    """
    Classe que representa um comportamento de exploração, onde o agente escolhe uma direção aleatória para se mover.
    Herda da classe Comportamento.
    """

    def activar(self, percepcao):
        """
        Método que ativa o comportamento de exploração.
        
        Args:
            percepcao: Percepção atual do ambiente pelo agente.
            
        Retorno:
            Resposta à percepção, que neste caso é uma RespostaMover com uma direção aleatória.
        """
        direcao = choice([direccao for direccao in Direccao])  # Escolhe aleatoriamente uma direção entre as disponíveis
        return RespostaMover(direcao).activar(percepcao)  # Ativa a resposta de mover com a direção escolhida e retorna a resposta