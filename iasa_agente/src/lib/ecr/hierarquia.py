from ecr.comport_comp import ComportComp


class Hierarquia(ComportComp):
    """
    Classe que representa um comportamento composto baseado em hierarquia, derivada da classe ComportComp.
    """

    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação com maior prioridade entre as ações fornecidas.

        :param accoes: Lista de ações para seleção.
        :return: Ação com a maior prioridade.
        """
        return accoes[0]
