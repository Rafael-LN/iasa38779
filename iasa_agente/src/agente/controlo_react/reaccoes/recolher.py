from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
    """
    Classe que representa um conjunto de comportamentos de recolha organizados de forma hierárquica.
    Herda da classe Hierarquia.
    """

    def __init__(self, comportamentos):
        """
        Método construtor da classe Recolher.
        
        Args:
            comportamentos (list): Lista de comportamentos que serão organizados hierarquicamente para a recolha.
        """
        super().__init__(comportamentos)  # Inicializa a classe pai (Hierarquia) com a lista de comportamentos fornecida.
        