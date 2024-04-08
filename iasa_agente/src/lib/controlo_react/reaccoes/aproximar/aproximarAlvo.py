from ecr.prioridade import Prioridade


class AproximarAlvo(Prioridade):
    """
    Classe que representa um conjunto de comportamentos de aproximação a um alvo consoante organizados por prioridade.
    Herda da classe Prioridade.
    """

    def __init__(self, comportamentos):
        """
        Método construtor da classe AproximarAlvo.
        
        Args:
            comportamentos (list): Lista de comportamentos que serão priorizados para a aproximação do alvo.
        """
        super().__init__(comportamentos)  # Inicializa a classe pai (Prioridade) com a lista de comportamentos fornecida.