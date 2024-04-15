from ecr.estimulo import Estimulo

class EstimuloAlvo(Estimulo):
    """
    Classe que representa um estímulo associado a um alvo em uma direção específica.
    Herda da classe Estimulo.
    """

    def __init__(self, direccao, gama=0.9):
        """
        Método construtor da classe EstimuloAlvo.
        
        Args:
            direccao (int): Direção do alvo.
            gama (float, opcional): Fator de desconto para o valor do estímulo (padrão é 0.9).
        """
        self.__direccao = direccao  # Direção do alvo
        self.__gama = gama  # Fator de desconto para o valor do estímulo

    def detectar(self, percepcao):
        """
        Método para detectar a presença do alvo na percepção.
        
        Args:
            percepcao (list): Percepção atual do ambiente.
            
        Returns:
            O valor do estímulo associado à presença do alvo na direção especificada.
        """
        if percepcao[self.__direccao] == "A":  # Se o alvo estiver presente na direção especificada
            return percepcao[1] ** self.__gama  # Retorna o valor do estímulo com desconto gamma
        return 0  # Retorna 0 se o alvo não estiver presente na direção especificada
