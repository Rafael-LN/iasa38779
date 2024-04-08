from sae.agente.controlo import Controlo


class ControloReact(Controlo):
    """
    Classe que representa um controlo reativo, derivada da classe Controlo.
    """

    def __init__(self, comportamento):
        """
        Método construtor da classe ControloReact.

        :param comportamento: Comportamento que será utilizado para processar as perceções.
        """
        self.__comportamento = comportamento
        
    def processar(self, percepcao):
        """
        Processa as perceções utilizando o comportamento fornecido.

        :param percepcao: Perceção a ser processada pelo controlo reativo.
        :return: Ação resultante do processamento das perceções.
        """
        return self.__comportamento.activar(percepcao)
