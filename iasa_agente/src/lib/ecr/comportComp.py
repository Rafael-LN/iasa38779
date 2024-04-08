from abc import abstractmethod
from ecr.comportamento import Comportamento


class ComportComp(Comportamento):
    """
    Classe que representa um comportamento composto, que consiste em uma combinação de comportamentos individuais.
    Herda da classe abstrata Comportamento.
    """

    def __init__(self, comportamentos):
        """
        Método construtor da classe ComportComp.
        
        Args:
            comportamentos (list): Lista de comportamentos individuais que compõem este comportamento composto.
        """
        self.__comportamentos = comportamentos
    
    def activar(self, percepcao):
        """
        Método que ativa o comportamento composto com base em uma percepção.
        
        Args:
            percepcao: A percepção atual do agente.
            
        Returns:
            Ação selecionada com base na percepção e nos comportamentos individuais ativos.
        """
        # Ativa cada comportamento individual e filtra os comportamentos que contêm uma acção
        accoes = [comportamento.activar(percepcao) for comportamento in self.__comportamentos if comportamento.activar(percepcao) is not None]
        
        # Verifica se existem ações não None
        if accoes:
            return self.seleccionar_accao(accoes)  # Seleciona uma ação com base nas ações disponíveis

    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Método abstrato para selecionar uma ação com base nas ações disponíveis.
        
        Args:
            accoes (list): Lista de ações disponíveis para seleção.
        
        Returns:
            Ação selecionada com base nas ações disponíveis.
        """
        pass